import os
import numpy as np
from PIL import Image, ImageDraw
import random as r


screen_x = 256
screen_y = 256
group_size = 50
generation_size = 1000
circle_number = 250


class Color(object):
    """
    RGBA模式，RGB三色通道，A透明度通道
    """
    def __init__(self):
        self.r = r.randint(0, 255)
        self.g = r.randint(0, 255)
        self.b = r.randint(0, 255)
        self.a = r.randint(95, 115)

    @staticmethod
    def copy(color):
        color_new = Color()
        color_new.r = color.r
        color_new.g = color.g
        color_new.b = color.b
        color_new.a = color.a
        return color_new


class Circle(object):
    def __init__(self):
        self.color = Color()              #随机初始化颜色值
        self.center_x = r.randint(0, screen_x)
        self.center_y = r.randint(0, screen_y)
        limits = [self.center_x, self.center_y,
                  (screen_x - self.center_x), (screen_y - self.center_y)]
        self.radius = r.randint(0, min(limits))

    def copy(self):
        color = Color.copy(self.color)
        circle_new = Circle()
        circle_new.center_y = self.center_y
        circle_new.center_x = self.center_x
        circle_new.radius = self.radius
        circle_new.color = color
        return circle_new


class CirclePic(object):
    def __init__(self):
        self.circles = []
        self.match = 0

    def add(self, circle):
        self.circles.append(circle)

    def get_img(self):
        return self.img

    def merge(self):
        if len(self.circles) < circle_number:
            print('circles are not enough')
            return
        self.img = Image.new('RGBA', size=(screen_x, screen_y))  # 新建一个画布
        draw_img = ImageDraw.Draw(self.img)  # 创建一个img图像上绘图的对象
        draw_img.polygon([(0, 0), (0, screen_y - 1), (screen_x - 1, screen_y - 1),
                          (screen_x - 1, 0)], fill=(254, 253, 255, 255))  # 绘制多边形，此处绘制了一个覆盖全画布大小的白色全不透明矩形，作为背景

        for circle in self.circles:
            circle_pic = Image.new('RGBA', size=(screen_x, screen_y))
            circle_img = ImageDraw.Draw(circle_pic)
            pos = (circle.center_x - circle.radius / 2, circle.center_y - circle.radius / 2,
                   circle.center_x + circle.radius / 2, circle.center_y + circle.radius / 2)
            # print(pos)
            circle_img.ellipse(pos, fill=(circle.color.r, circle.color.g, circle.color.b, circle.color.a))
            self.img = Image.alpha_composite(self.img, circle_pic)

    def get_match_value(self):
        return self.match

    def cal_match(self):
        gene_pixel = np.array([])  # 生成图像的像素向量
        for p in self.img.split()[:-1]:  # split获得一个元组，包含RGBA四个Image对象，[:-1]用来选取前三个结果，即对象的RGB值
            gene_pixel = np.hstack((gene_pixel, np.hstack(np.array(p))))
        # np.array(p)将p对象转化为numpy类型的数组， np.hstack()可将矩阵按行合并为一维向量
        target_pixel = np.array([])
        for p in target_img.split()[:-1]:
            target_pixel = np.hstack((target_pixel, np.hstack(np.array(p))))

        self.match = np.sum(np.square(np.subtract(gene_pixel, target_pixel)))

    def get_circle_by_index(self, index):
        return self.circles[index].copy()

    @staticmethod
    def get_mutate_circle_pic(circle_pic):
        new_circle_pic = CirclePic()
        for circle in circle_pic.circles:
            if 0.2 > r.random():
                new_circle = Circle()
                new_circle_pic.add(new_circle)
            else:
                new_circle = circle.copy()
                new_circle_pic.add(new_circle)
        return new_circle_pic


class CircleGroup(object):
    factor = 5

    def __init__(self):
        self.size = int(group_size/CircleGroup.factor)
        self.exchange_times = CircleGroup.factor - 2
        self.mutate_number = group_size - self.size * (self.exchange_times + 1)
        self.circle_pics = []

    def insert(self, circle_pic):
        if not self.circle_pics:
            self.circle_pics.append(circle_pic)
            return
        for i in range(len(self.circle_pics)):
            if circle_pic.get_match_value() < self.circle_pics[i].get_match_value():
                if len(self.circle_pics) == self.size:
                    self.circle_pics.pop()
                self.circle_pics.insert(i, circle_pic)
            else:
                if len(self.circle_pics) < self.size:
                    self.circle_pics.append(circle_pic)

    def exchange(self):
        new_group = []
        # print('circle pics ', len(self.circle_pics))
        for circle_father in self.circle_pics:
            for i in range(self.exchange_times):
                circle_mother = r.choice(self.circle_pics)
                circle_kid = CirclePic()
                for j in range(circle_number):
                    if 0.5 > r.random():
                        circle_kid.add(circle_father.get_circle_by_index(j))
                    else:
                        circle_kid.add(circle_mother.get_circle_by_index(j))
                new_group.append(circle_kid)
        # print('new group is ', len(new_group))
        self.circle_pics.extend(new_group)

    def mutate(self):
        new_group = []
        for i in range(self.mutate_number):
            # print(len(self.circle_pics))
            mutate_cicrcle_pic = r.choice(self.circle_pics)
            new_circle_pic = CirclePic.get_mutate_circle_pic(mutate_cicrcle_pic)
            new_group.append(new_circle_pic)
        self.circle_pics.extend(new_group)

    def check(self):
        # print(len(self.circle_pics))
        return len(self.circle_pics) == group_size


def select(result_address):
    each_group = None
    for i in range(generation_size):
        print('generation is ', i)
        if i == 0:
            circle_group = CircleGroup()
            for inital_elem in range(group_size):
                circle_pic = CirclePic()
                for circle_index in range(circle_number):
                    circle_pic.add(Circle())
                circle_pic.merge()
                circle_pic.cal_match()
                circle_group.insert(circle_pic)
            circle_group.exchange()
            circle_group.mutate()
            if circle_group.check():
                each_group = circle_group
            else:
                print('error')
                return
        else:
            circle_group = CircleGroup()
            for circle_pic in each_group.circle_pics:
                circle_pic.merge()
                circle_pic.cal_match()
                circle_group.insert(circle_pic)
            circle_group.exchange()
            circle_group.mutate()
            if circle_group.check():
                each_group = circle_group
            else:
                print('error')
        if i % 50 == 0:     # 每迭代100代就输出一次环境适应度值，并保存当前父代图像到本地
            top_circle_img = each_group.circle_pics[0].get_img()
            top_circle_img.save(os.path.join(result_address, '%d.png' % (i)))
            print('match is ', each_group.circle_pics[0].get_match_value())


result_address = r'D:\pic\circle'
target_address = r'D:\pic\target.jpeg'
target_img = Image.open(target_address).resize((256, 256)).convert("RGBA")

if __name__ == '__main__':        # 运行主函数
    select(result_address)






