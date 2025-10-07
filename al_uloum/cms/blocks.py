"""Custom blocks StreamField"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail_blocks import blocks as wagtail_blocks


# Create your blocks here.
class ContentBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    accordion = wagtail_blocks.AccordionBlock(help_text=_("Accordion"))
    alert = wagtail_blocks.AlertBlock(help_text=_("Alert"))
    document = DocumentChooserBlock(help_text=_("Document"))
    image = wagtail_blocks.ImageBlock(help_text=_("Image"))
    list = wagtail_blocks.ListBlock(help_text=_("List"))
    quote = blocks.BlockQuoteBlock(help_text=_("Quote"))
    text = blocks.RichTextBlock(help_text=_("Text"))
    tabs = wagtail_blocks.TabsBlock(help_text=_("Tabs"))
    timeline = wagtail_blocks.TimelineBlock(help_text=_("Timeline"))
    video = EmbedBlock(help_text=_("Video"))
