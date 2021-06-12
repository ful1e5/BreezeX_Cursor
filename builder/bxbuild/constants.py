#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

# Info
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/BreezeX_Cursor"

# XCursor
X_DELAY: int = 10


# Windows Cursor
WIN_DELAY = 1


# TODO: add coordinates
X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    ##########
    # Static #
    ##########
    "all-scroll.png": {"xhot": 100, "yhot": 100},
    "bd_double_arrow.png": {"xhot": 100, "yhot": 100},
    "bottom_left_corner.png": {"xhot": 100, "yhot": 100},
    "bottom_right_corner.png": {"xhot": 100, "yhot": 100},
    "bottom_side.png": {"xhot": 100, "yhot": 100},
    "center_ptr.png": {"xhot": 100, "yhot": 100},
    "col-resize.png": {"xhot": 100, "yhot": 100},
    "context-menu.png": {"xhot": 100, "yhot": 100},
    "copy.png": {"xhot": 100, "yhot": 100},
    "cross.png": {"xhot": 100, "yhot": 100},
    "crossed_circle.png": {"xhot": 100, "yhot": 100},
    "dnd_no_drop.png": {"xhot": 100, "yhot": 100},
    "dotbox.png": {"xhot": 100, "yhot": 100},
    "fd_double_arrow.png": {"xhot": 100, "yhot": 100},
    "hand1.png": {"xhot": 100, "yhot": 100},
    "hand2.png": {"xhot": 100, "yhot": 100},
    "left_ptr.png": {"xhot": 100, "yhot": 100},
    "left_side.png": {"xhot": 100, "yhot": 100},
    "link.png": {"xhot": 100, "yhot": 100},
    "move.png": {"xhot": 100, "yhot": 100},
    "pencil.png": {"xhot": 100, "yhot": 100},
    "pirate.png": {"xhot": 100, "yhot": 100},
    "plus.png": {"xhot": 100, "yhot": 100},
    "question_arrow.png": {"xhot": 100, "yhot": 100},
    "right_ptr.png": {"xhot": 100, "yhot": 100},
    "row-resize.png": {"xhot": 100, "yhot": 100},
    "right_side.png": {"xhot": 100, "yhot": 100},
    "sb_down_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_h_double_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_left_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_right_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_up_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_v_double_arrow.png": {"xhot": 100, "yhot": 100},
    "top_left_corner.png": {"xhot": 100, "yhot": 100},
    "top_right_corner.png": {"xhot": 100, "yhot": 100},
    "top_side.png": {"xhot": 100, "yhot": 100},
    "vertical-text.png": {"xhot": 100, "yhot": 100},
    "wayland-cursor.png": {"xhot": 100, "yhot": 100},
    "X_cursor.png": {"xhot": 100, "yhot": 100},
    "xterm.png": {"xhot": 100, "yhot": 100},
    "zoom-in.png": {"xhot": 100, "yhot": 100},
    "zoom-out.png": {"xhot": 100, "yhot": 100},
    ############
    # Animated #
    ############
    # NOTE: Animated cursors don't need an extension and frame numbers.
    "left_ptr_watch": {"xhot": 100, "yhot": 100},
    "wait": {"xhot": 100, "yhot": 100},
}

# TODO setting windows cursors
WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    ##########
    # Static #
    ##########
    "right_ptr.png": {"to": "Alternate", "position": "top_right"},
    "cross.png": {"to": "Cross"},
    "left_ptr.png": {"to": "Default", "position": "top_left"},
    "bottom_right_corner.png": {"to": "Diagonal_1"},
    "bottom_left_corner.png": {"to": "Diagonal_2"},
    "pencil.png": {"to": "Handwriting"},
    "question_arrow.png": {"to": "Help", "position": "top_left"},
    "sb_h_double_arrow.png": {"to": "Horizontal"},
    "xterm.png": {"to": "IBeam", "position": "top_left"},
    "hand2.png": {"to": "Link", "position": "top_left"},
    "hand1.png": {"to": "Move"},
    "dnd_no_drop.png": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow.png": {"to": "Vertical"},
    ############
    # Animated #
    ############
    # NOTE: Animated cursors don't need frame numbers.
    "left_ptr_watch": {"to": "Work", "position": "top_left"},
    "wait": {"to": "Busy"},
}
