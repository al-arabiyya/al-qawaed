"""Page models"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page as WagtailPage
from wagtail.search import index

from al_uloum.cms.blocks import ContentBlock


# Create your models here.
class Page(WagtailPage):
    """Pages: Pages to partition big grammars"""

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

    context_object_name = "page"
    template = "al_uloum/page.html"
    parent_page_types = ["al_uloum_indexes.SubIndex", "al_uloum_sections.Section"]
    subpage_types = []

    api_fields = [APIField("description"), APIField("content")]
    content_panels = WagtailPage.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
    ]
    search_fields = WagtailPage.search_fields + [
        index.SearchField("description"),
        index.SearchField("content"),
    ]
