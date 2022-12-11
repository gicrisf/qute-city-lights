clr = {
    "bg": "#1D252C", # bg
    "bg-alt": "#171D22", #bg-alt
    "bg-alt-256": "#111122", #bg-alt (256)
    "bg-selected": "#10151C", #bg-selected
    "bg-lightened": "#41505e", #bg-lightened
    "fg-disabled": "#56697a", #fg-disabled
    "fg": "#a0b3c5", #base05 (white-ish, cadet-blue-crayola)
    "cbc-alt": "#9CAABB", # base08 (white-ish, cadet-blue alt), unused
    "fg-alt": "#728ca0", #base06 (bright white, light-slate-gray), unused
    "maya-blue": "#5ec4ff", # blue
    "paradise-pink": "#d95468", # red
    "persian-orange": "#D98E48", # orange
    "gold-crayola": "#EBBF83", # yellow
    "celadon": "#8BD49C", # green
    "dark-cyan": "#008b94", # dark cyan
    "cornflower-blue": "#539AFC", # bright blue
    "shimmering-blush": "#e27e8d", # magenta
    "maroon-x11": "#b62d65", # violet
    "electric-blue": "#70E1E8", # cyan (extra)
}

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = clr["fg"]

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = clr["bg-alt"]

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = clr["bg"]

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = clr["cornflower-blue"]

# Background color of the completion widget category headers.
c.colors.completion.category.bg = clr["bg"]

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = clr["bg"]

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = clr["bg"]

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = clr["electric-blue"]

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = clr["bg-selected"]

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = clr["bg-selected"]

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = clr["bg-selected"]

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = clr["persian-orange"]

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = clr["gold-crayola"]

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = clr["fg"]

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = clr["bg"]

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = clr["bg-alt"]

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = clr["fg-disabled"]

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = clr["bg"]

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  clr["fg"]

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = clr["bg-selected"]

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = clr["fg"]

# Background color for the download bar.
c.colors.downloads.bar.bg = clr["bg"]

# Color gradient start for download text.
c.colors.downloads.start.fg = clr["bg"]

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = clr["cornflower-blue"]

# Color gradient end for download text.
c.colors.downloads.stop.fg = clr["bg"]

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = clr["dark-cyan"]

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = clr["paradise-pink"]

# Font color for hints.
c.colors.hints.fg = clr["bg"]

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = clr["gold-crayola"]

# Font color for the matched part of hints.
c.colors.hints.match.fg = clr["fg"]

# Text color for the keyhint widget.
c.colors.keyhint.fg = clr["fg"]

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = clr["gold-crayola"]

# Background color of the keyhint widget.
c.colors.keyhint.bg = clr["bg"]

# Foreground color of an error message.
c.colors.messages.error.fg = clr["bg"]

# Background color of an error message.
c.colors.messages.error.bg = clr["paradise-pink"]

# Border color of an error message.
c.colors.messages.error.border = clr["paradise-pink"]

# Foreground color of a warning message.
c.colors.messages.warning.fg = clr["bg"]

# Background color of a warning message.
c.colors.messages.warning.bg = clr["shimmering-blush"]

# Border color of a warning message.
c.colors.messages.warning.border = clr["shimmering-blush"]

# Foreground color of an info message.
c.colors.messages.info.fg = clr["fg"]

# Background color of an info message.
c.colors.messages.info.bg = clr["bg-alt-256"] # ex. bg

# Border color of an info message.
c.colors.messages.info.border = clr["bg-alt-256"] # ex. bg

# Foreground color for prompts.
c.colors.prompts.fg = clr["fg"]

# Border used around UI elements in prompts.
c.colors.prompts.border = clr["bg"]

# Background color for prompts.
c.colors.prompts.bg = clr["bg"]

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = clr["bg-selected"]

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = clr["fg"]

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = clr["celadon"]

# Background color of the statusbar.
c.colors.statusbar.normal.bg = clr["bg"]

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = clr["bg"]

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = clr["cornflower-blue"]

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = clr["bg"]

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = clr["dark-cyan"]

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = clr["bg"]

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = clr["bg-alt"]

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = clr["fg"]

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = clr["bg"]

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = clr["fg"]

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = clr["bg"]

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = clr["bg"]

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = clr["maroon-x11"]

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = clr["bg"]

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = clr["cornflower-blue"]

# Background color of the progress bar.
c.colors.statusbar.progress.bg = clr["cornflower-blue"]

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = clr["fg"]

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = clr["paradise-pink"]

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = clr["electric-blue"] # ex. cadet blue crayola

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = clr["fg"]

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = clr["celadon"]

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = clr["shimmering-blush"]

# Background color of the tab bar.
c.colors.tabs.bar.bg = clr["bg"]

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = clr["cornflower-blue"]

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = clr["dark-cyan"]

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = clr["paradise-pink"]

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = clr["fg"]

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = clr["bg-selected"]

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = clr["fg"]

# Background color of unselected even tabs.
c.colors.tabs.even.bg = clr["bg-selected"]

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = clr["bg-selected"]

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = clr["fg"]

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = clr["bg-selected"]

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = clr["fg"]

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = clr["bg-lightened"]

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = clr["fg"]

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = clr["bg-lightened"]

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = clr["fg"]

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = clr["fg"]

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = clr["bg-lightened"]

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = clr["fg"]

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = clr["bg-lightened"]

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = clr["bg"]
