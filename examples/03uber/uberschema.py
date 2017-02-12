# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Product(Schema):
    product_id = fields.String(description='Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.')
    description = fields.String(description='Description of product.')
    display_name = fields.String(description='Display name of product.')
    capacity = fields.Integer(description='Capacity of product. For example, 4 people.')
    image = fields.String(description='Image URL representing the product.')


class ProductList(Schema):
    products = fields.List(fields.Field('Product'), description='Contains the list of products')


class PriceEstimate(Schema):
    product_id = fields.String(description='Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles')
    currency_code = fields.String(description='[ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency code.')
    display_name = fields.String(description='Display name of product.')
    estimate = fields.String(description='Formatted string of estimate in local currency of the start location. Estimate could be a range, a single number (flat rate) or "Metered" for TAXI.')
    low_estimate = fields.Number(description='Lower bound of the estimated price.')
    high_estimate = fields.Number(description='Upper bound of the estimated price.')
    surge_multiplier = fields.Number(description='Expected surge multiplier. Surge is active if surge_multiplier is greater than 1. Price estimate already factors in the surge multiplier.')


class Profile(Schema):
    first_name = fields.String(description='First name of the Uber user.')
    last_name = fields.String(description='Last name of the Uber user.')
    email = fields.String(description='Email address of the Uber user')
    picture = fields.String(description='Image URL of the Uber user.')
    promo_code = fields.String(description='Promo code of the Uber user.')


class Activity(Schema):
    uuid = fields.String(description='Unique identifier for the activity')


class Activities(Schema):
    offset = fields.Integer(description='Position in pagination.')
    limit = fields.Integer(description='Number of items to retrieve (100 max).')
    count = fields.Integer(description='Total number of items available.')
    history = fields.List(fields.Field('Activity'))


class Error(Schema):
    code = fields.Integer()
    message = fields.String()
    fields = fields.String()


class ProductsInput(object):
    class Get(object):
        """
        Product Types
        """

        class Query(Schema):
            latitude = fields.Number(description='Latitude component of location.')
            longitude = fields.Number(description='Longitude component of location.')




class EstimatesPriceInput(object):
    class Get(object):
        """
        Price Estimates
        """

        class Query(Schema):
            start_latitude = fields.Number(description='Latitude component of start location.')
            start_longitude = fields.Number(description='Longitude component of start location.')
            end_latitude = fields.Number(description='Latitude component of end location.')
            end_longitude = fields.Number(description='Longitude component of end location.')




class EstimatesTimeInput(object):
    class Get(object):
        """
        Time Estimates
        """

        class Query(Schema):
            start_latitude = fields.Number(description='Latitude component of start location.')
            start_longitude = fields.Number(description='Longitude component of start location.')
            customer_uuid = fields.UUID(description='Unique customer identifier to be used for experience customization.')
            product_id = fields.String(description='Unique identifier representing a specific product for a given latitude & longitude.')




class HistoryInput(object):
    class Get(object):
        """
        User Activity
        """

        class Query(Schema):
            offset = fields.Integer(description='Offset the list of returned results by this amount. Default is zero.')
            limit = fields.Integer(description='Number of items to retrieve. Default is 5, maximum is 100.')




class ProductsOutput(object):
    class Get200(Product):
        """An array of products"""

        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Getdefault(Error):
        """Unexpected error"""
        pass



class EstimatesPriceOutput(object):
    class Get200(PriceEstimate):
        """An array of price estimates by product"""

        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Getdefault(Error):
        """Unexpected error"""
        pass



class EstimatesTimeOutput(object):
    class Get200(Product):
        """An array of products"""

        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Getdefault(Error):
        """Unexpected error"""
        pass



class MeOutput(object):
    class Get200(Profile):
        """Profile information for a user"""
        pass

    class Getdefault(Error):
        """Unexpected error"""
        pass



class HistoryOutput(object):
    class Get200(Activities):
        """History information for the given user"""
        pass

    class Getdefault(Error):
        """Unexpected error"""
        pass
