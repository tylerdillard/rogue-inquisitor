def clean(scroll_name):

    invalid = '<>:"/\|?*'

    for char in invalid:
	    scroll_name = scroll_name.replace(char, '')
	
    return (scroll_name)