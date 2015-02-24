from selenium.webdriver.common.by import By

class MainPageLocators(object):

    BUY_BUTTON = (".btn-buy-now.block.breathe-vertical")                # Buy now button
    SIGN_IN_LINK = ("#signInLink>#signInLink")                          # Sign in Link
    USER_NAME_FIELD = ("login_username")                                # Username element
    PASSWORD_FIELD = ("login_password")                                 # Password element
    LOGIN_BUTTON = ("input[value='Sign in']")                           # Sign in button in login page
    CHECKOUT_BUTTON = (".btn-primary.block")                            # Check out button
    DROPDOWN_ARROW = (".nav-dropdown-arrow")                            # Drop down arrow
    SIGN_OUT = (".my-account>ul>li>a[href*='logout']")                  # Sign out in drop down
    FAVORITED_MORE = (".favs-truncated")                                # Favorited by more element
    FAVORITES_TOTAL = ("#favorite-count")                               # Favorites total
    FAVORITES_IMAGE = ("#youFavorite>a>img")                            # Favorite small image
    FAV_N_WISHLIST = (".my-account>ul>li>a[href*='favorites']")         # Favorites & Wishlist element
    WHITE_PRODUCT = (".product-config-chooser.hide-tablet>div>.swatch-menu>.breathe-bottom-large>.swatch-grid>.swatch-box[title*='White']>.swatch>img")     # White product little button
    BLACK_PRODUCT = (".product-config-chooser.hide-tablet>div>.swatch-menu>.breathe-bottom-large>.swatch-grid>.swatch-box[title*='Black']>.swatch>img")     # Black product little button
    FAVORITES_ICON = (".product-share-bar.breathe-vertical-large.hide-tablet.hide-mobile>.shapeways-community-social.clearfix>.add-to-list>.breathe-right>.icon-favorite")          # Favorites icon
    FAVORITE_TEXT = (".product-share-bar.breathe-vertical-large.hide-tablet.hide-mobile>.shapeways-community-social.clearfix>.add-to-list>.breathe-right>span")                     # Favorite text
    ART_ICON = (".keywords>a[href='/art']")                             # Art icon
    ACCESSORIES1_ICON = (".keywords>a[href*='for-your-home/accessories']")                  # Accessories1 icon
    ACCESSORIES2_ICON = (".keywords>a[href*='tag=accessories']")        # Accessories2 icon
    SCULPTURES_ICON = (".keywords>a[href*='sculptures']")               # Sculptures icon
    BEER_ICON = (".keywords>a[href*='Beer']")                           # Beer icon
    GRUMPY_ICON = (".keywords>a[href*='Grumpy']")                       # Grumpy icon
    HOME_ICON = (".keywords>a[href*='tag=home']")                       # Home icon
    HOMEBREW_ICON = (".keywords>a[href*='Homebrew']")                   # Homebrew icon
    GADGETS_ICON = (".dropdown>a[href*='gadgets']")                     # Gadgets icon at the top of the page
    ACCESSORIES_TOP_ICON = (".dropdown>a[href*='accessories']")         # Accessories icon at the top of the page
    JEWELRY_ICON = (".dropdown>a[href*='jewelry']")                     # Jewelry icon at the top of the page
    ART_TOP_ICON = (".dropdown>a[href*='art']")                         # Art icon at the top of the page
    HOME_TOP_ICON = (".dropdown>a[href*='home']")                       # Home icon at the top of the page
    GAMES_TOP_ICON = (".dropdown>a[href*='games']")                     # Games icon at the top of the page
    MINIATURES_ICON = (".dropdown>a[href*='miniatures']")               # Miniatures icon at the top of the page
    BETA_TOP_ICON = (".inner>ul>li>a[href*='beta']")                    # Beta icon at the top of the page
    MY_LITTLE_PONY_ICON = (".inner>ul>li>a[href*='pony']")              # My little pony icon at the top of the page
    GIFT_TOP_ICON = (".dropdown>a[href*='gift']")                       # Gift icon at the top of the page
    APPS_TOP_ICON = (".dropdown>a[href*='creator']")                    # Apps icon at the top of the page
    FEED_TOP_ICON = (".inner>ul>li>a[href*='feed']")                    # Feed icon at the top of the page
    BLOG_TOP_ICON = (".inner>ul>li>a[href*='blog']")                    # Blog icon at the top of the page
    NOTIFICATIONS_DROPDOWN = (".my-account>ul>li>a[href*='notifications']")                 # Notifications option top right dropdown menu
    MYFEED_DROPDOWN = (".my-account>ul>li>a[href*='feed']")             # My feed option top right dropdown menu
    ORDERS_DROPDOWN = (".my-account>ul>li>a[href*='orders']")           # Orders option top right dropdown menu
    MODELS_DROPDOWN = (".my-account>ul>li>a[href*='models']")           # Models option top right dropdown menu
    PROFILE_DROPDOWN = (".my-account>ul>li>a[href*='designer']")        # Public profile option top right dropdown menu
    SETTINGS_DROPDOWN = (".my-account>ul>li>a[href*='settings']")       # Settings option top right dropdown menu
    ABOUT_US_FOOTER = ("#footer-about>ul>li>a[href*='about']")          # About us link at the page footer
    HOW_WORKS_FOOTER = ("#footer-about>ul>li>a[href*='works']")         # How the company works link at the page footer
    PRESS_FOOTER = ("#footer-about>ul>li>a[href*='press']")             # Press link at the page footer
    CONTACT_US_FOOTER = ("#footer-about>ul>li>a[href*='contact']")      # Contact us link at the page footer
    CAREERS_FOOTER = ("#footer-about>ul>li>a[href*='jobs']")            # Careers link at the page footer
    DEVELOPERS_FOOTER = ("#footer-about>ul>li>a[href*='dev']")          # Developers link at the page footer
    HELP_CENTER_FOOTER = ("#footer-help>ul>li>a[href*='support?']")     # Help Center link at the page footer
    CONTACT_SUPPORT_FOOTER = ("#footer-help>ul>li>a[href*='service']")  # Contact Support link at the page footer
    FAQ_FOOTER = ("#footer-help>ul>li>a[href*='faq']")                  # FAQs link at the page footer
    SHIPPING_INFO_FOOTER = ("#footer-help>ul>li>a[href*='shipping']")   # Shipping Info link at the page footer
    TUTORIALS_FOOTER = ("#footer-help>ul>li>a[href*='tutorials']")      # Tutorials link at the page footer
    TWITTER_FOOTER = (".icon-twitter.footer-icon")                      # Twitter icon at the page footer
    FLICKR_FOOTER = (".icon-flickr.footer-icon")                        # Flickr icon at the page footer
    MEETUP_FOOTER = (".icon-meetup.footer-icon")                        # Meetup icon at the page footer
    FACEBOOK_FOOTER = (".icon-facebook.footer-icon")                    # Facebook icon at the page footer
    TUMBLR_FOOTER = (".icon-tumblr.footer-icon")                        # Tumblr icon at the page footer
    YOUTUBE_FOOTER = (".icon-youtube.footer-icon.last")                 # Youtube icon at the page footer
    USERNAME_TWITTER_FOOTER = (".username")                             # Twitter username link at the page footer
    QUOTE_FOOTER = (".quote>p>a[href*='shpws']")                        # Quote link at the page footer
    TWITTER_PIC_FOOTER = (".quote>p>a[href*='twitter']")                # Twitter pic link at the page footer
    PRIVACY_FOOTER = (".privacy>a")                                     # Privacy link at the page legal footer
    TERMS_FOOTER = (".terms>a")                                         # Terms and Conditions link at the page legal footer
    POLICY_FOOTER = (".policy>a")                                       # Policy link at the page legal footer
    SHOP_ICON = (".active")                                             # Shop link at the top left side of the screen
    DESIGN_ICON = (".nav-tab.left>a[href*='create']")                   # Design link at the top left side of the screen
    SELL_ICON = (".nav-tab.left>a[href*='shop']")                       # Sell link at the top left side of the screen
    WISH_ICON = (".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social.clearfix>\
    .add-to-list>a[data-sw-add-list='wishlist']>.icon-wishlist")        # Wishlist icon
    WISHLISTED = (".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social.clearfix>\
    .add-to-list>a[href*='wishlist']>span")                             # Wishlist text
    ADD_TO_LIST = (".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social.clearfix>\
    .add-to-list>#addToListLink")                                       # AddtoList element
    FACEBOOK_ICON = ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social>\
    .social-product-bar>.facebook>a[title*='Face']>.icon-facebook"      # Facebook icon
    TWITTER_ICON = ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social>\
    .social-product-bar>.twitter>.twitter-share-button>.icon-twitter"   # Twitter icon
    PINTEREST_ICON = ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social>\
    .social-product-bar>.pinterest>a[title*='Share']>.icon-pinterest"   # Pinterest icon
    QUESTIONMARK = ".product-config-chooser.hide-tablet>div[data-sw-product-configuration-chooser='DM8QHNHJS']>\
    .swatch-menu>.swatch-label>#ftp-tool-tip"                           # Questionmark symbol on element
    LEARN_MORE = ".ftp-tool-tip-link"                                   # Learn more icon
    BIG_BASKET = ".shop-avatar.breathe-right-large>a>img"               # Big basket image
    TEST_ALL_THE_THINGS = ".hide-mobile>.visit-shop.viewmore-arrow"     # Test all the things icon
    CODETEST = ".go-to-designer>a"                                      # Shapeways Codetests element
    VISIT_SHOP = ".send-message>.visit-shop.viewmore-arrow"             # Visit shop icon
    COUNTRY_FLAG = ".country-flag>img"                                  # Country Flag icon
    CURRENCY_SYMBOL_ID = "current-currency-symbol"                      # Currency Symbol field
    CURRENCY_COUNTRY_ID = "autocompleteCountry"                         # Currency Country field
    SUBMIT_ID = "submitChangeCountryCurrency"                           # Submit Country Currency Button
    PRICE_FIELD = ".product-config-chooser.hide-tablet>.material-selected>\
    .material-list-item-selected.product-info>.price.bottom-collapse"   # Price on top of buy button




class OtherPageLocators(object):

    BIG_FAVORITE_IMAGE = (".product-url>img")                           # Image of favorited product
    BIG_FAV_N_WISH_IMG = (".product-url>img[src*='1355847178.jpg']")    # Image in Favorites & Wishlist page
    REMOVE_FAVORITE = (".remove-model>a")                               # Remove favorite n wishlist button
    NOTIFICATIONS_TAG = (".span-12>h1")                                 # Tag in the notifications page
    MYFEED_TAG = (".tab.tab-my-feed.active>a[href*='feed']")            # Tag in the my feed page
    ORDERS_TAG = (".container.my-orders>h1")                            # Tag in the my orders page
    MODELS_TAG = (".results-header.clearfix>h1")                        # Tag in the my models page
    PROFILE_TAG = (".username.shop-title-header")                       # Tag in the public profile page
    FAV_N_WISH_TAG = (".wishlist-summary.wishlist-summary-selected>a")  # Tag in the Favorite n Wishlist page
    SETTINGS_TAG = ("#useraccount_form>h1")                             # Tag in the Settings page
    WISH_TAB = (".wishlist-summary>a[href*='wishlist']")                # Wishlist tab
    WISH_IMAGE = (".product-url>img")                                   # Wishlist image
    ADD_LIST_FIELD = ("add-list")                                       # Add list field
    CREATE_LIST_BUTTON = ("add-new-list-button")                        # Create new list button
    DONE_LIST_BUTTON_ID = ("custom-list-done")                          # Done list button
    MANAGE_LISTS_ID = ("manage-lists-link")                             # Manage Lists element
    DONE_MANAGE = (".secondary-button-inset[value='Done']")             # Done button element inside Manage lists
    DELETE_LIST = (".delete-list[onclick*='test']")                     # Delete list button
    CLOSE_LISTS = (".close-button[onclick*='fancy']")                   # Close icon inside manage lists
    OTHER_LISTS_ID = ("customLists")                                    # Other lists field
    LIST_DROP_DOWN = ("#customLists>option[value='test']")              # List in the drop down menu
    BLACK_DESCRIPTION = (".material.hash-7360379")                      # Description for the black product
    BLACK_REMOVE = (".remove-model>a[hashid='7360379']")                # Remove button for the black product
    WHITE_DESCRIPTION = (".material.hash-7360377")                      # Description for the white product
    WHITE_REMOVE = (".remove-model>a[hashid='7360377']")                # Remove button for the white product




    locators = {
    "css_signin_link": "#signInLink>#signInLink",
    "id_username":  "login_username",
    "id_password": "login_password",
    "css_loginbutton": "input[value='Sign in']",
    "css_favorited_more": ".favs-truncated",
    "css_favorites_total": "#favorite-count",
    "css_favorite_icon": ".product-share-bar.breathe-vertical-large.hide-tablet.hide-mobile>.shapeways-community-social.clearfix>.add-to-list>.breathe-right>.icon-favorite",
    "css_favorite_text": ".product-share-bar.breathe-vertical-large.hide-tablet.hide-mobile>.shapeways-community-social.clearfix>.add-to-list>.breathe-right>span",
    "css_favorite_small_img": "#youFavorite>a>img",
    "css_image_big_favorite_pg": ".product-url>img",
    "css_dropdown_arrow": ".nav-dropdown-arrow",
    "css_favorites_wishlist": ".my-account>ul>li>a[href*='favorites']",
    "css_image_in_favor_n_wish": ".product-url>img[src*='1355847178.jpg']",
    "css_remove_favorite": ".remove-model>a",
    "css_sign_out": ".my-account>ul>li>a[href*='logout']",
    "css_add_to_list": ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social.clearfix>.add-to-list>#addToListLink",
    "id_add_list_field": "add-list",
    "id_add_new_list": "add-new-list-button",
    "css_delete_list": ".delete-list",
    "css_donebtn_inside_list": ".secondary-button-inset[value='Done']",
    "css_accessories2_icon": ".keywords>a[href*='tag=accessories']",
    "css_accessories_icon": ".keywords>a[href*='for-your-home/accessories']",
    "css_art_icon": ".keywords>a[href='/art']",
    "css_sculptures_icon": ".keywords>a[href*='sculptures']",
    "css_gift_guide": ".btn-primary",                       # Gift guide
    "css_buy_button": ".btn-buy-now.block.breathe-vertical",
    "css_checkout": ".btn-primary.block",
    "css_silver_box": "#checkout-confirm-giftwrap-option-radio-5",                  # Silver box radio button
    "css_giftwrap_conf": "#checkout-confirm-giftwrap-option-radio-5",               # Gift wrap confirm radio button
    "css_gift_msg_button": "#hasGiftMessage",               # Gift message radio button
    "css_gift_text": "itemGiftMessage",                     # Gift text area
    "css_remain_chars": ".message-counter>.chars-remaining",                        # Remaining charactes and lines
    "css_remove_button": ".item-action-links>a",            # Remove button
    "css_grumpy_icon": ".keywords>a[href*='Grumpy']",
    "css_home_icon": ".keywords>a[href*='tag=home']",
    "css_home_tag": ".search-results-query-count.span-12>h2",                       # Home tag
    "css_homebrew": ".keywords>a[href*='Homebrew']",
    "css_leftside_box": ".box-gray",                        # Left side box icon
    "css_slide_thumb_img1": ".slideshow-thumb.product-slideshow-thumb>img[src*='1355847627.jpg']",          # Slide thumb image 1
    "css_slide_big1": "#slideshow-big>.film-strip-img[src*='1355847627.jpg']",      # Slide big image 1
    "css_slide_thumb_img2": ".slideshow-thumb.product-slideshow-thumb>img[src*='1355847631.jpg']",          # Slide thumb image 2
    "css_slide_big2": "#slideshow-big>.film-strip-img[src*='1355847631.jpg']",      # Slide big image 2
    "css_slide_thumb_img3": ".slideshow-thumb.product-slideshow-thumb>img[src*='1408794831.jpg']",          # Slide thumb image 3
    "css_slide_big3": "#slideshow-big>.film-strip-img[src*='1408794831.jpg']",      # Slide big image 3
    "css_slide_thumb_img4": ".slideshow-thumb.product-slideshow-thumb>img[src*='1408794841.jpg']",          # Slide thumb image 4
    "css_slide_big4": "#slideshow-big>.film-strip-img[src*='1408794841.jpg']",      # Slide big image 4
    "css_slide_thumb_img5": ".slideshow-thumb.product-slideshow-thumb>img[src*='1355847178.jpg']",          # Slide thumb image 5
    "css_slide_big5": "#slideshow-big>.film-strip-img[src*='1355847178.jpg']",      # Slide big image 5
    "css_right_arrow": ".slideshow-right-arrow.enabled",    # Slideshow right arrow
    "css_slide_thumb_3d": ".slideshow-thumb.product-slideshow-thumb>img[src*='3d-thumbnail.jpg']",           # Slide thumb 3d image
    "css_cube_doom": ".product-url>img[alt*='DOOOOOOM']",   #Cube of Doom icon element
    "css_cube_big_img": "#slideshow-big>.film-strip-img[src*='1408795456']",        # Cube of doom big image
    "css_cube_img2": "#slideshow-big>.film-strip-img[src*='1355937615']",           # Cube of doom image2
    "css_cube_3rd": ".slideshow-thumb.product-slideshow-thumb>img[alt*='Model']",   # 3rd image in the slideshow
    "css_blk_str_flx": ".product-config-chooser.hide-tablet>div>.swatch-menu>.breathe-bottom-large>.swatch-grid>.swatch-box[title*='Black']>.swatch>img",          # Black Strong and Flexible little button element
    "css_little_pony": ".inner>ul>li>a[href*='mylittlepony']",                      # My Little Pony element
    "css_fcb_icon": ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social>.social-product-bar>.facebook>a[title*='Face']>.icon-facebook",
    "css_twitter_icon": ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social>.social-product-bar>.twitter>.twitter-share-button>.icon-twitter",
    "css_pin_icon": ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social>.social-product-bar>.pinterest>a[title*='Share']>.icon-pinterest",
    "css_test_all_icon": ".shop-avatar.breathe-right-large>a>img[alt*='Test']",     # Test all the things image element
    "css_happy_cube": ".product-url>img[alt='A Happy Cube']",                       # Happy cube image element
    "id_ship_251": "shipping-option-251",                   # Ship 251 option
    "css_ship_value": ".shippingCost",                      # Shipping cost value element
    "css_sub_total": ".itemSubtotal",                       # Subtotal value element
    "css_grand_total": ".col.col4>.grandTotal>strong>.grandTotal>strong",           # Grand total element
    "css_grand_total2": ".grandTotal>strong",               # Grand total element2
    "css_grand_total3": ".grandTotal>strong",               # Grand total element3
    "css_grand_total4": ".grandTotal>strong",               # Grand total element4
    "id_ship_215": "shipping-option-215",                   # Ship 215 option
    "id_ship_242": "shipping-option-242",                   # Ship 242 option
    "id_ship_243": "shipping-option-243",                   # Ship 243 option
    "css_2nd_cat": ".slideshow-thumb.product-slideshow-thumb>img[src*='1355847631']",            # Second cat image
    "css_utube": ".youtube>.play",                          # Youtube play element
    "css_price_buy": ".product-config-chooser.hide-tablet>.material-selected>.material-list-item-selected.product-info>.price.bottom-collapse",
    "css_sub_pop": ".tally-total-col-r>strong",             # Subtotal element on the top right corner inside the pop-up
    "css_wish_icon": ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social.clearfix>.add-to-list>a[data-sw-add-list='wishlist']>.icon-wishlist",
    "css_wish_text": ".product-share-bar.breathe-vertical-large.hide-tablet>.shapeways-community-social.clearfix>.add-to-list>a[href*='wishlist']>span",
    "css_wish_tab": ".wishlist-summary>a[href*='wishlist']",
    "css_wish_img": ".product-url>img"
    }

class SearchResultsPageLocators(object):
    pass