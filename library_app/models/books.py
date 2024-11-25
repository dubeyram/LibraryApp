# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
from datetime import timedelta, datetime
# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from .timestampable import TimeStampable

class Book(TimeStampable):
    """
    Description of Book Model
    """

    name = models.CharField(verbose_name=_("Name"), max_length=128)
    author = models.CharField(
        verbose_name=_("Author"),
        max_length=255,
    )
    book_price = MoneyField(
        verbose_name=_("Book Price"),
        decimal_places=2,
        default=100,
        default_currency="INR",
        max_digits=16,
    )
    in_stock = models.BooleanField(
        verbose_name=_("In Stock"),
        default=True,
        help_text=_("Availabile or Not"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("About the book"),
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        default=0,
        null=True,
        blank=True,
        help_text=_("Quantity of the book"),
    )

    class Meta:
        app_label = "library_app"
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
