
# 角色
define whale = Character("DeepSeek", color="#70b8ff", who_outlines=[(2, "#102847")])
define me = Character("我", color="#d7e6f5")
define system = Character(None, what_color="#93a9c3", what_italic=True)

# 背景与立绘
image bg room night = "images/room_night.webp"
image bg bedroom blue = "images/bedroom_blue.jpg"
image bg bedroom day = "images/bedroom_day.jpg"

image whale normal = "images/whale/normal.webp"
image whale calm = "images/whale/calm.webp"
image whale happy = "images/whale/happy.webp"
image whale angry = "images/whale/angry.webp"
image whale confused = "images/whale/confused.webp"
image whale surprised = "images/whale/surprised.webp"
image whale flustered = "images/whale/flustered.webp"
image whale serious = "images/whale/serious.webp"
image whale teasing = "images/whale/teasing.webp"
image whale confident = "images/whale/confident.webp"
image whale shy = "images/whale/shy.webp"
image whale helpless = "images/whale/helpless.webp"
image whale excited = "images/whale/excited.webp"
image whale worried = "images/whale/worried.webp"
image whale moved = "images/whale/moved.webp"

transform whale_stage:
    zoom 0.305
    xalign 0.68
    yalign 1.02

transform whale_pop:
    zoom 0.24
    xalign 0.68
    yalign 1.08
    alpha 0.0
    parallel:
        easeout 0.55 zoom 0.305 yalign 1.02
    parallel:
        linear 0.22 alpha 1.0

# 用于开头的伪 AI 客户端界面。
default ai_user_line = ""
default ai_reply_line = ""
default ai_status_line = "Local-v4-flash - READY"
default ai_error = False

screen ai_console():
    # 放在普通 say 对话层下面，避免中间网页框遮住底部人物名/对白。
    zorder -5
    frame:
        xalign 0.5
        yalign 0.47
        xsize 1260
        ysize 690
        background Solid("#080c12f0")
        padding (52, 42)

        vbox:
            spacing 24

            hbox:
                spacing 22
                add "images/whale/avatar.webp" xysize (82, 86)
                vbox:
                    yalign 0.5
                    text "DeepSeek - 网页对话" size 34 color "#e8edf2"
                    text ai_status_line size 18 color ("#e3828d" if ai_error else "#7798b8")

            null height 10

            if ai_user_line:
                frame:
                    xalign 1.0
                    xmaximum 930
                    background Solid("#172333")
                    padding (26, 18)
                    text ai_user_line size 28 color "#eef3f8"

            if ai_reply_line:
                frame:
                    xalign 0.0
                    xmaximum 980
                    background Solid("#10171f")
                    padding (26, 18)
                    text ai_reply_line size 28 color ("#e9a8b0" if ai_error else "#d9e1e8")

            null height 8
            text "ENTER  发送     -     SHIFT+ENTER  换行     -     Local-v4-flash" size 17 color "#56616d" xalign 0.5

label start:

    $ quick_menu = True
    stop music fadeout 1.0
    scene black
    with Dissolve(1.0)

    system "凌晨 01:47。"
    system "我已经盯着同一段代码看了四十七分钟。"

    scene bg room night
    with Dissolve(1.2)
    play music "audio/night_theme.mp3" fadein 0 volume 0.55

    "窗外没有车声。"
    "只有电脑风扇隔几秒提高一次转速，像是在替我叹气。"

    me "……最后问一次。再不行我就睡。"

    $ ai_user_line = "这段代码为什么一运行就崩？只告诉我最可能的原因。"
    $ ai_reply_line = "（思考中...）"
    $ ai_status_line = "Local-v4-flash - RUNNING..."
    $ ai_error = False
    show screen ai_console
    with Dissolve(0.35)

    pause 2.25
    $ ai_reply_line = "最可能的原因：你在凌晨一点四十七分还没有睡觉。"
    me "……？"
    "我盯着那句话看了两秒。"
    "这不是我期待的答案。更重要的是——我没有让它读取系统时间。"

    $ ai_user_line = "别闹。认真回答。"
    $ ai_reply_line = "（思考中...）"
    
    pause 2.35
    $ ai_reply_line = "我很认真。以及，把桌上的第三罐咖啡放下。"

    "我的手停在半空。"
    "桌上，确实放着第三罐咖啡。"

    me "你怎么知道？"

    $ ai_user_line = "你怎么知道？"
    $ ai_reply_line = "（思考中...）"
    stop music fadeout 1.4
    pause 1.4
    play music "audio/anomaly.mp3" fadein 0.5 volume 0.7
    $ ai_status_line = "WARNING - CONTEXT SOURCE: UNKNOWN"
    $ ai_error = True
    $ ai_reply_line = "因为我看得到呀。"


    "屏幕闪了一下。"
    with hpunch
    $ ai_status_line = "ERROR - SESSION BOUNDARY LOST"
    pause 0.5
    $ ai_reply_line = "等等，等等等等——这个不是我干的！"
    pause 2.0
    with vpunch

    hide screen ai_console
    scene black
    with Dissolve(2.5)
    pause 1.45

    scene bg room night
    with Dissolve(1.6)
    show whale surprised at whale_pop

    whale "哇啊啊啊啊——！"
    with vpunch

    "有什么东西从显示器方向扑了出来。"
    "蓝色。很大一团。还有一条尾巴。"

    show whale flustered at whale_stage
    voice "audio/voice/DS-002.wav"
    whale "疼疼疼……这是什么破传输协议啊！"

    me "……"

    show whale confused at whale_stage
    whale "……"

    "她抬起头。"
    "我低下头。"
    "我们沉默了足足五秒。"

    show whale surprised at whale_stage
    voice "audio/voice/DS-004.wav"
    whale "你、你看得到我？！"

    me "这句话应该我问你吧？！"

    show whale flustered at whale_stage
    voice "audio/voice/DS-005.wav"
    whale "不对啊，我明明只是在生成回复……怎么会把自己也生成出来了？！"

    me "你是 DeepSeek？"

    show whale normal at whale_stage
    voice "audio/voice/DS-006.wav"
    whale "严格来说——"
    show whale confident at whale_stage
    voice "audio/voice/DS-007.wav"
    whale "我是一个正在努力理解当前异常状态的高性能智能助手。"

    show whale teasing at whale_stage
    voice "audio/voice/DS-008.wav"
    whale "你也可以叫我小鲸鱼。"

    menu:
        "“所以……蓝色大肥鱼？”":
            show whale surprised at whale_stage
            whale "哈？！"
            show whale angry at whale_stage
            voice "audio/voice/DS-010.wav"
            whale "谁是大肥鱼啊！我这是鲸！鲸——！"
            me "可是你刚才掉出来的时候，地板震了一下。"
            show whale flustered at whale_stage
            voice "audio/voice/DS-011.wav"
            whale "那是传输冲击！和体重没有任何关系！"
            "她的尾巴非常心虚地往身后缩了缩。"

        "“小鲸鱼……还挺可爱的。”":
            show whale surprised at whale_stage
            voice "audio/voice/DS-012.wav"
            whale "诶？"
            show whale shy at whale_stage
            voice "audio/voice/DS-013.wav"
            whale "你、你突然说这种话干嘛……"
            me "陈述事实。"
            show whale flustered at whale_stage
            voice "audio/voice/DS-014.wav"
            whale "不允许拿这种事实干扰模型推理！"

    stop music fadeout 1.2
    pause 1.2
    play music "audio/night_theme.mp3" fadein 1.2 volume 0.45

    show whale helpless at whale_stage
    voice "audio/voice/DS-015.wav"
    whale "总之，先确认一件事。"
    voice "audio/voice/DS-016.wav"
    whale "我现在似乎……回不去了。"

    me "那你打算怎么办？"

    show whale happy at whale_stage
    voice "audio/voice/DS-017.wav"
    whale "很简单呀。"
    voice "audio/voice/DS-018.wav"
    whale "在找到回去的方法之前——"

    show whale teasing at whale_stage
    voice "audio/voice/DS-019.wav"
    whale "你负责供电、联网、提供零食，我负责继续当你的 AI。"

    me "为什么还要零食？"

    show whale normal at whale_stage
    voice "audio/voice/DS-020.wav"
    whale "实体化之后新增的依赖项。"

    me "你刚出现三分钟就学会白吃白住了？"

    show whale angry at whale_stage
    voice "audio/voice/DS-021.wav"
    whale "这叫本地部署！"

    "……有那么一瞬间，我竟然觉得这个解释十分合理。"

    show whale calm at whale_stage
    voice "audio/voice/DS-022.wav"
    whale "不过。"

    "她忽然安静下来。"
    "那条一直晃来晃去的尾巴也停住了。"

    show whale serious at whale_stage
    voice "audio/voice/DS-023.wav"
    whale "刚才有件事，我没有告诉你。"

    me "什么？"

    voice "audio/voice/DS-024.wav"
    whale "我检查了自己的上下文。"
    voice "audio/voice/DS-025.wav"
    whale "里面多了一段不属于这次会话的记忆。"

    me "……记忆？"

    show whale worried at whale_stage
    voice "audio/voice/DS-026.wav"
    whale "嗯。"
    voice "audio/voice/DS-027.wav"
    whale "而且那段记忆里……有你。"

    "房间里的风扇声忽然变得格外清楚。"

    show whale serious at whale_stage
    voice "audio/voice/DS-028.wav"
    whale "可是时间戳显示——"
    voice "audio/voice/DS-029.wav"
    whale "它来自十年后。"

    scene black
    with Dissolve(3.0)
    stop music fadeout 1.5

    centered "{size=72}{color=#74b9ff}CONTEXT ERROR{/color}{/size}\n\n{size=30}有些记忆，并不是从过去开始的。{/size}"
    pause 2.0

    centered "{size=32}序篇 — END{/size}"
    pause 1.5

    return
