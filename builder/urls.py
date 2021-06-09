from .renderer import *

class Page:
    def __init__(self, path, renderer, data_more=None):
        self.path = path
        self.renderer = renderer
        self.data_more = data_more

def get_safe_path(pathname):
    if pathname.endswith('.html'):
        return pathname
    else:
        return '%s/index.html' % pathname

def get_pages(data):
    for website_personal in data['personal']:
        print(website_personal)
    print("HIHI")
    return [
        Page('index.html', render_index),
        Page('members.html', render_members),
        Page('research.html', render_research),
        Page('links.html', render_links),
        Page('contact.html', render_contact),
    ] + [
        Page(
            get_safe_path(page['path']), 
            lambda x: render_page(x, page),
        ) for page in data['pages']
    ] + [
        Page(
            get_safe_path(redirect['path']), 
            lambda x: render_redirect(x, redirect),
        ) for redirect in data['redirects']
    ] + [
        Page(
            get_safe_path(website_personal['path']), 
            lambda x: render_personal_website(x, website_personal),
            data_more = website_personal
        ) for website_personal in data['personal']
    ]
