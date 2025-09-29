# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

# https://qauto2.forstudy.space/
locators_main = [
    {
        "x_pass_short": "//a[@class='header_logo']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/a",
        "css_short": "app-header .header_logo",
        "css_full": "body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > a"
    },
    {
        "x_pass_short": "//a[contains(@class, 'header-link') and normalize-space(text())='Home']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/a",
        "css_short": "a.btn.header-link",
        "css_full": "body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > a"
    },
    {
        "x_pass_short": "//button[@appscrollto='aboutSection']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[1]",
        "css_short": "[appscrollto='aboutSection']",
        "css_full": "body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(2)"
    },
    {
        "x_pass_short": "//button[@class='header-link -guest']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[1]",
        "css_short": "button.header-link.-guest",
        "css_full": "body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.header-link.-guest"
    },
    {
        "x_pass_short": "//button[contains(@class, 'btn-primary') and text()='Sign up']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]",
        "css_short": "button.header_signin",
        "css_full": "body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.btn.btn-outline-white.header_signin"
    },
    {
        "x_pass_short": "//button[contains(@class, 'hero-descriptor_btn') and text()='Sign up']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button",
        "css_short": ".hero-descriptor .btn-primary",
        "css_full": "body > app-root > app-global-layout > div > div > div > app-guest-layout > div > app-home > section > div > div > div.col-12.col-lg-4 > div > button"
    },
    {
        "x_pass_short": "//button[contains(@class, 'ytp-large-play-button') and @aria-label='Play']",
        "x_pass_full": "/html/body/div/div/div[5]/button",
        "css_short": ".ytp-large-play-button[aria-label='Play']",
        "css_full": "#movie_player > div.ytp-cued-thumbnail-overlay > button"
    },
    {
        "x_pass_short": "//img[contains(@src, 'info_1.jpg') and @alt='Instructions']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[1]/div/div/div[1]/div/div/img",
        "css_short": "img[src*='info_1.jpg']",
        "css_full": "#aboutSection > div > div > div:nth-child(1) > div > div > img"
    },
    {
        "x_pass_short": "//p[contains(@class, 'about-block_title') and normalize-space(text())='Log fuel expenses']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[1]/div/div/div[1]/div/p[1]",
        "css_short": "#aboutSection div.col-lg-6:not(.mt-lg-0) p.about-block_title.h2",
        "css_full": "#aboutSection > div > div > div:nth-child(1) > div > p.about-block_title.h2"
    },
    {
        "x_pass_short": "//p[contains(@class, 'about-block_title') and normalize-space(text())='Instructions and manuals']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[1]/div/div/div[2]/div/p[1]",
        "css_short": "#aboutSection div.mt-lg-0 p.about-block_title.h2",
        "css_full": "#aboutSection > div > div > div.col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3 > div > p.about-block_title.h2"
    },
    {
        "x_pass_short": "//div[@id='contactsSection']//h2[normalize-space()='Contacts']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[2]/div/div/div[1]/h2",
        "css_short": "#contactsSection .col-md-6 > h2",
        "css_full": "#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > h2"
    },
    {
        "x_pass_short": "//a[contains(@href, 'facebook.com') and contains(@class, 'socials_link')]",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[2]/div/div/div[1]/div/a[1]",
        "css_short": "#contactsSection a[href*='facebook.com']",
        "css_full": "#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-start > div > a:nth-child(1)"
    },
    {
        "x_pass_short": "//a[@href='https://ithillel.ua' and contains(@class, 'contacts_link')]",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[2]/div/div/div[2]/a[1]",
        "css_short": "a[href='https://ithillel.ua']",
        "css_full": "#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-end.justify-content-md-end.mb-2.mt-3.mt-md-0 > a.contacts_link.display-4"
    },
    {
        "x_pass_short": "//a[@href='mailto:developer@ithillel.ua']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/div[2]/div/div/div[2]/a[2]",
        "css_short": "a[href^='mailto:developer@ithillel.ua']",
        "css_full": "#contactsSection > div > div > div.col-md-6.d-flex.flex-column.align-items-center.align-items-md-end.justify-content-md-end.mb-2.mt-3.mt-md-0 > a.contacts_link.h4"
    },
    {
        "x_pass_short": "//footer[contains(@class, 'footer')]",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/app-footer/footer",
        "css_short": "app-footer .footer",
        "css_full": "body > app-root > app-global-layout > div > app-footer > footer"
    },
    {
        "x_pass_short": "//a[contains(@class, 'footer_logo')]/*[name()='svg']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/app-footer/footer/div/div/div[2]/a/svg",
        "css_short": ".footer_item.-right svg",
        "css_full": "body > app-root > app-global-layout > div > app-footer > footer > div > div > div.col.footer_item.-right > a > svg"
    }
]

# https://qauto2.forstudy.space/panel/instructions
locators_panel_instructions = [
    {
        "x_pass_short": "//button[@id='userNavDropdown']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/button",
        "css_short": "#userNavDropdown",
        "css_full": "#userNavDropdown"
    },
    {
        "x_pass_short": "//button[@id='userNavDropdown']//img",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/button/img",
        "css_short": "#userNavDropdown img",
        "css_full": "#userNavDropdown > img"
    },
    {
        "x_pass_short": "//div[contains(@class, 'header_left')]//a[@routerlink='/panel/garage']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div/nav/a[1]",
        "css_short": "a.header-link[href='/panel/garage']",
        "css_full": "body > app-root > app-global-layout > div > div > app-header > header > div > div > div > nav > a:nth-child(1)"
    },
    {
        "x_pass_short": "//nav[contains(@class, 'sidebar')]//a[@routerlink='instructions']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[3]",
        "css_short": "a.sidebar_btn[href='/panel/instructions']",
        "css_full": "body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-3.d-none.d-lg-block.sidebar-wrapper > nav > a.btn.btn-white.btn-sidebar.sidebar_btn.-active"
    },
    {
        "x_pass_short": "//button[@id = 'brandSelectDropdown']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-instructions/div/div[2]/div/div[1]/app-instructions-search-controls/div/div[1]/button",
        "css_short": "#brandSelectDropdown",
        "css_full": "#brandSelectDropdown"
    },
    {
        "x_pass_short": "//button[contains(@class, 'instructions-search-controls_search')]",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-instructions/div/div[2]/div/div[1]/app-instructions-search-controls/div/button",
        "css_short": "button.instructions-search-controls_search",
        "css_full": "body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-lg-9.main-wrapper > div > app-instructions > div > div.panel-page_content > div > div.instructions_header > app-instructions-search-controls > div > button"
    },
    {
        "x_pass_short": "//p[contains(text(), 'Front windshield wipers')]/following-sibling::a[contains(@class, 'instruction-link_download')]",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-instructions/div/div[2]/div/div[2]/ul/li[1]/a/a",
        "css_short": ".instructions_content li:first-child  a.instruction-link_download",
        "css_full": "body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-lg-9.main-wrapper > div > app-instructions > div > div.panel-page_content > div > div.instructions_content > ul > li:nth-child(1) > a > a"
    },
    {
        "x_pass_short": "//p[contains(text(), 'Front windshield wipers')]/ancestor::a[contains(@class, 'instruction-link')]",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-instructions/div/div[2]/div/div[2]/ul/li[1]/a",
        "css_short": "a.instruction-link[href*='Front windshield wipers']",
        "css_full": "body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-lg-9.main-wrapper > div > app-instructions > div > div.panel-page_content > div > div.instructions_content > ul > li:nth-child(1) > a"
    },
    {
        "x_pass_short": "//nav[contains(@class, 'sidebar')]//a[normalize-space(text())='Log out']",
        "x_pass_full": "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[4]",
        "css_short": ".sidebar .btn.text-danger",
        "css_full": "body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-3.d-none.d-lg-block.sidebar-wrapper > nav > a.btn.btn-link.text-danger.btn-sidebar.sidebar_btn"
    }
]
