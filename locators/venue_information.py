class VenueInformation:
    button_change_logo                  = '//XCUIElementTypeButton[@name="Change logo"]'
    input_venue_name                    = '//XCUIElementTypeTextField[@name="Venue name"]'
    text_area_about_venue               = '//XCUIElementTypeTextField[@name="About venue"]'
    button_edit_venue_location          = '//XCUIElementTypeButton[@name="Edit venue location"]'
    image_venue                         = '//XCUIElementTypeStaticText[@name="Venue images"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeImage'
    button_x_venue_image                = '//XCUIElementTypeStaticText[@name="Venue images"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeImage/following-sibling::XCUIElementTypeOther'
    icon_image                          = '//XCUIElementTypeButton[@name="Change logo"]/preceding-sibling::XCUIElementTypeImage[1]'

    ## location
    icon_maps_location                  = '//XCUIElementTypeOther[@name="staticmap 300×300 pixels"]/XCUIElementTypeImage'


    button_save_venue_information       = '//XCUIElementTypeButton[@name="Save venue information"]'