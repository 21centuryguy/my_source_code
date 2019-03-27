import clipboard
clipboard.copy("111")  # now the clipboard content will be string "abc"
clipboard.copy("222")
clipboard.copy("333")
clipboard.copy("444")
clipboard.copy("555")

text_from_clipboard = clipboard.paste()  # text will have the content of clipboard
print(text_from_clipboard)
