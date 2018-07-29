from django import template

from wagtail.images.models import Image

from bakerydemo.base.models import Horse

register = template.Library()

@register.simple_tag()
def get_horses(horse_type):

    horse_list = None
    if horse_type == 'stallion':
        horse_list = Horse.objects.filter(sex='M', status = 'NFS')
    elif horse_type == 'mare':
        horse_list = Horse.objects.filter(sex='F', status = 'NFS')
    elif horse_type == 'forsale':
        horse_list = Horse.objects.filter(status='FS')
    elif horse_type == 'sale':
        horse_list = Horse.objects.filter(status='S')

    return horse_list

@register.simple_tag()
def get_horse_images(collection):
    image_list = Image.objects.filter(collection=collection)
    return image_list
