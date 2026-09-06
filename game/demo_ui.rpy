# Dark minimalist UI overrides.

init 100:

    style main_menu_frame:
        background None
        xfill True
        yfill True

    style main_menu_vbox:
        xalign 0.0
        xoffset 92
        yalign 0.135
        yoffset 0
        xmaximum 820
        spacing 10

    style main_menu_title:
        color "#f3f6f9"
        size 52
        outlines []
        kerning 1

    style main_menu_subtitle:
        color "#b7c3cf"
        size 27
        outlines []
        kerning 1

    style main_menu_subsubtitle:
        color "#71808f"
        size 19
        outlines []
        kerning 0.5

    style navigation_button:
        xsize 320
        ysize 58
        background None
        hover_background Solid("#ffffff0d")
        selected_background Solid("#ffffff0d")
        left_padding 16
        right_padding 16

    style navigation_button_text:
        size 27
        color "#8d98a5"
        hover_color "#f4f8fc"
        selected_color "#f4f8fc"
        insensitive_color "#59616b88"
        xalign 0.0

    style window:
        background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

    style namebox:
        background None
        padding (0, 0)

    style say_label:
        color "#7fc2ff"
        size 32
        outlines []

    style say_dialogue:
        color "#e2e8ef"
        size 30
        outlines []
        line_spacing 7

    style quick_menu:
        xalign 0.985
        yalign 0.992
        spacing 2

    style quick_button:
        background None
        hover_background Solid("#ffffff0a")
        xpadding 8
        ypadding 5

    style quick_button_text:
        size 17
        color "#56616d"
        hover_color "#aeb9c5"
        selected_color "#7fc2ff"

    style choice_vbox:
        xalign 0.5
        ypos 430
        yanchor 0.5
        spacing 14

    style choice_button:
        background Frame("gui/button/choice_idle_background.png", Borders(14, 14, 14, 14))
        hover_background Frame("gui/button/choice_hover_background.png", Borders(14, 14, 14, 14))
        xsize 1080
        xpadding 28
        ypadding 18

    style choice_button_text:
        color "#cbd4dd"
        hover_color "#ffffff"
        size 28
        xalign 0.5

    style game_menu_outer_frame:
        background Solid("#070a0edb")
        bottom_padding 54
        top_padding 150

    style game_menu_navigation_frame:
        xsize 365
        yfill True

    style game_menu_content_frame:
        left_margin 44
        right_margin 58
        top_margin 8

    style game_menu_label:
        xpos 92
        ysize 135

    style game_menu_label_text:
        size 46
        color "#f1f5f8"
        yalign 0.5

    style return_button:
        xpos 92
        yalign 1.0
        yoffset -48

    style gui_label_text:
        color "#dce3ea"

    style gui_text:
        color "#c7d0d9"

    style slot_button:
        background Frame("gui/button/slot_idle_background.png", Borders(14,14,14,14))
        hover_background Frame("gui/button/slot_hover_background.png", Borders(14,14,14,14))

    style slot_button_text:
        color "#8f9aa6"
        hover_color "#dfe6ed"

    style page_button:
        background None
        hover_background Solid("#ffffff0b")

    style page_button_text:
        color "#727e8b"
        hover_color "#ecf2f8"
        selected_color "#7fc2ff"

    style pref_label_text:
        color "#dce3ea"
        size 27

    style radio_button:
        background None
        hover_background Solid("#ffffff0a")

    style check_button:
        background None
        hover_background Solid("#ffffff0a")

    style radio_button_text:
        color "#8e99a5"
        hover_color "#eef4fa"
        selected_color "#7fc2ff"

    style check_button_text:
        color "#8e99a5"
        hover_color "#eef4fa"
        selected_color "#7fc2ff"

    style about_text:
        color "#aeb8c2"
        line_spacing 5

    style history_text:
        color "#cbd3dc"

    style history_name_text:
        color "#7fc2ff"

    style confirm_frame:
        background Frame("gui/frame.png", Borders(20,20,20,20))

    style confirm_prompt_text:
        color "#eef3f8"

    style confirm_button:
        background None
        hover_background Solid("#ffffff0d")

    style confirm_button_text:
        color "#9aa6b2"
        hover_color "#ffffff"
