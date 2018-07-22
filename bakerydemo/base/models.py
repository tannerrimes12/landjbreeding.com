from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import BaseStreamBlock


class Breed(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name


class Horse(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    sex = models.CharField(max_length = 1, choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    ), default = 'M')
    breed = models.ForeignKey('Breed', models.SET_DEFAULT, default = Breed.objects.get(name='Unknown').pk)
    # breed = models.ForeignKey('Breed', models.SET_NULL, null = True, blank = True)
    status = models.CharField(max_length = 3, choices = (
        ('FS', 'For Sale'),
        ('S', 'Sold'),
        ('NFS', 'Not For Sale'),
    ), default = 'NFS')


    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('breed'),
        FieldPanel('sex'),
        FieldPanel('status'),

    ]




class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]


class HomePage(Page):
    """
    The Home Page. This looks slightly more complicated than it is. You can
    see if you visit your site and edit the homepage that it is split between
    a:
    - Hero area
    - Body area
    - A promotional area
    - Moveable featured site sections
    """

    # Hero section of HomePage
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    hero_text = models.CharField(
        max_length=255,
        help_text='Write an introduction for the bakery'
        )
    hero_cta = models.CharField(
        verbose_name='Hero CTA',
        max_length=255,
        help_text='Text to display on Call to Action'
        )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text='Choose a page to link to for the Call to Action'
    )

    # Body section of the HomePage
    body = StreamField(
        BaseStreamBlock(), verbose_name="Home content block", blank=True
    )

    # Promo section of the HomePage
    # promo_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Promo image'
    # )
    # promo_title = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # promo_text = RichTextField(
    #     null=True,
    #     blank=True,
    #     help_text='Write some promotional copy'
    # )

    # Featured sections on the HomePage
    # You will see on templates/base/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    # featured_section_1_title = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # featured_section_1 = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='First featured section for the homepage. Will display up to '
    #     'three child items.',
    #     verbose_name='Featured section 1'
    # )
    #
    # featured_section_2_title = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # featured_section_2 = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Second featured section for the homepage. Will display up to '
    #     'three child items.',
    #     verbose_name='Featured section 2'
    # )
    #
    # featured_section_3_title = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # featured_section_3 = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Third featured section for the homepage. Will display up to '
    #     'six child items.',
    #     verbose_name='Featured section 3'
    # )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('hero_text', classname="full"),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                PageChooserPanel('hero_cta_link'),
                ])
            ], heading="Hero section"),
        # MultiFieldPanel([
        #     ImageChooserPanel('promo_image'),
        #     FieldPanel('promo_title'),
        #     FieldPanel('promo_text'),
        # ], heading="Promo section"),
        StreamFieldPanel('body'),
        # MultiFieldPanel([
        #     MultiFieldPanel([
        #         FieldPanel('featured_section_1_title'),
        #         PageChooserPanel('featured_section_1'),
        #         ]),
        #     MultiFieldPanel([
        #         FieldPanel('featured_section_2_title'),
        #         PageChooserPanel('featured_section_2'),
        #         ]),
        #     MultiFieldPanel([
        #         FieldPanel('featured_section_3_title'),
        #         PageChooserPanel('featured_section_3'),
        #         ])
        # ], heading="Featured homepage sections", classname="collapsible")
    ]

    def __str__(self):
        return self.title


class GalleryPage(Page):
    """
    This is a page to list locations from the selected Collection. We use a Q
    object to list any Collection created (/admin/collections/) even if they
    contain no items. In this demo we use it for a GalleryPage,
    and is intended to show the extensibility of this aspect of Wagtail
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    collection = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=['Root']),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Select the image collection for this gallery.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
        FieldPanel('collection'),
    ]

    # Defining what content type can sit under the parent. Since it's a blank
    # array no subpage can be added
    subpage_types = []


class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    http://docs.wagtail.io/en/latest/reference/contrib/forms/index.html
    """
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(BaseStreamBlock())
    thank_you_text = RichTextField(blank=True)

    # Note how we include the FormField object via an InlinePanel using the
    # related_name value
    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
