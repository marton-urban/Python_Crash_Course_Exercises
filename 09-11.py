from modules.users import Admin

special_admin = Admin('Marci', 'Urbánka', 33, 'Hungary', 'Fucking')
special_admin.privileges.list_of_privileges = ['ez is', 'az is', 'de még amaz is']
special_admin.privileges.show_privileges()
