"""Index models"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from al_uloum.cms.blocks import ContentBlock


# Create your models here.
class Index(Page):
    """Al Uloum index page"""

    content = StreamField(
        ContentBlock(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "index"
    template = "al_uloum/index.html"
    parent_page_types = ["home.Home"]
    subpage_types = ["al_uloum_indexes.SubIndex"]

    api_fields = [APIField("content")]
    content_panels = Page.content_panels + [FieldPanel("content")]
    search_fields = Page.search_fields + [index.SearchField("content")]


class SubIndex(Page):
    """Index page for each science"""

    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Page description"),
    )
    content = StreamField(
        ContentBlock(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "index"
    template = "al_uloum/subindex.html"
    parent_page_types = ["al_uloum_indexes.Index"]
    subpage_types = ["al_uloum_sections.Section", "al_uloum_pages.Page"]

    api_fields = [APIField("description"), APIField("content")]
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("content"),
    ]
