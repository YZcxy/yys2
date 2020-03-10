class CommonPos():
    second_position = (1000, 100), (1111, 452)  # 第二次结算所点击的位置

    @staticmethod
    def InitPosWithClient__():
        for item in vars(CommonPos).items():
            if not '__' in item[0]:
                setattr(CommonPos, item[0], ((
                    item[1][0][0], item[1][0][1] + 35), (item[1][1][0], item[1][1][1] + 35)))


class TansuoPos():
    last_chapter = (934, 493), (1108, 572)  # 列表最后一章
    quit_last_chapter = (913, 114), (948, 148)  # 退出最后一章
    tansuo_btn = (787, 458), (890, 500)  # 探索按钮
    tansuo_denglong = (424, 118), (462, 158)  # 探索灯笼
    ready_btn = (1000, 460), (1069, 513)  # 准备按钮
    quit_btn = (32, 45), (58, 64)  # 退出副本
    confirm_btn = (636, 350), (739, 370)  # 退出确认按钮
    change_monster = (427, 419), (457, 452)  # 切换狗粮点击区域
    quanbu_btn = (37, 574), (80, 604)  # “全部”按钮
    n_tab_btn = (142, 288), (164, 312)  # n卡标签
    s_tab_btn = (33, 264), (82, 307)  # 素材标签
    r_tab_btn = (216, 322), (259, 366)  # r卡标签
    n_slide = (168, 615), (784, 615)  # n卡进度条，从头至尾
    gouliang_left = (161, 174), (322, 288)  # 左边狗粮位置
    gouliang_middle = (397, 218), (500, 349)  # 中间狗粮位置
    gouliang_right = (628, 293), (730, 430)  # 右边狗粮位置
    gouliang_leftback = (0, 273), (150, 393)  # 左后狗粮位置
    gouliang_rightback = (433, 462), (567, 569)  # 右后狗粮位置
    yaoqing_comfirm = (601, 361), (746, 406)  # 继续邀请按钮

    @staticmethod
    def InitPosWithClient__():
        for item in vars(TansuoPos).items():
            if not '__' in item[0]:
                setattr(TansuoPos, item[0], ((
                    item[1][0][0], item[1][0][1] + 35), (item[1][1][0], item[1][1][1] + 35)))


class YuhunPos():
    tiaozhan_btn = (995, 533), (1055, 595)    # 御魂挑战按钮
    kaishizhandou_btn = (1048, 535), (1113, 604)   # 御魂开始战斗按钮
    yuhun_menu = (148, 568), (206, 620)    # 御魂菜单
    yuhun_btn = (147, 152), (327, 408)    # 御魂选项
    yeyuanhuo_btn = (476, 125), (708, 427)    # 业原火选项
    beimihu_btn = (838, 141), (1048, 407)    # 卑弥呼

    @staticmethod
    def InitPosWithClient__():
        for item in vars(YuhunPos).items():
            if not '__' in item[0]:
                setattr(YuhunPos, item[0], ((
                    item[1][0][0], item[1][0][1] + 35), (item[1][1][0], item[1][1][1] + 35)))


class BreakthroughPos():
    # 结界突破位置
    target_position = (((117, 80), (410, 195)),
                       ((422, 80), (718, 195)),
                       ((728, 80), (1023, 195)),
                       ((117, 202), (410, 315)),
                       ((422, 202), (718, 315)),
                       ((728, 202), (1023, 315)),
                       ((117, 322), (410, 434)),
                       ((422, 322), (718, 434)),
                       ((728, 322), (1023, 434)))  # 六组突破目标位置
    refresh_position = ((858, 458), (1007, 503)) # 刷新按钮位置
    confirm_btn = ((600, 362), (750, 408)) # 确认刷新按钮
    jiesuan_position = (90, 20), (425, 70)  # 结算位置，防止误点，范围很小
    # 寮突破位置
    shack_target_position = (((365, 95), (660, 207)),
                            ((665, 95), (960, 207)),
                            ((365, 215), (660, 327)),
                            ((665, 215), (960, 327)),
                            ((365, 335), (660, 447)),
                            ((665, 335), (960, 447)),
                            ((365, 455), (660, 567)),
                            ((665, 455), (960, 567)))    # 八组突破目标位置

    quit_btn = (22, 20), (42, 40)  # 退出战斗
    confirm_quit_btn = (615, 363), (702, 386)  # 退出确认按钮
