# config.py = configuration data 

#---------------------------------------------------------------------

APP_DATE_FORMAT = "%Y-%b-%d"

# port we are running on
PORT=9050

# title on web pages
APP_TITLE = "Poliquiz"
APP_LOGO = "<i class='fa fa-times-rectangle-o'></i> "

# unique identifier for the app, typically the same as its directory 
# in ~/proj/ .
# Usually also used for MongoDB database name
APP_NAME = "poliquiz"
DB_NAME = "poliquiz"

# create an admin site?
CREATE_ADMIN_SITE=True
# prefix in urls for the admin site
ADMIN_SITE_PREFIX="dbv"

#---------------------------------------------------------------------


#end
