def module_namespace_checker(target_from_tk_menu):

	if target_from_tk_menu == "scikit-learn":
		target_from_tk_menu = "sklearn"
		print("scikit-learn -> ", target_from_tk_menu)
		
	if target_from_tk_menu == "Pillow":
		target_from_tk_menu = "PIL"
		print("Pillow -> ", target_from_tk_menu)

	if target_from_tk_menu == "absl-py":
		target_from_tk_menu = "absl"
		print("absl-py -> ", target_from_tk_menu)

	else:
		target_from_tk_menu = target_from_tk_menu.lower()

	return target_from_tk_menu

if __name__ == "__main__":
	module_namespace_checker()
