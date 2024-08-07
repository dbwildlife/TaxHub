from marshmallow import pre_load, fields
from marshmallow_sqlalchemy.fields import RelatedList
from marshmallow_sqlalchemy import auto_field

from utils_flask_sqla.schema import SmartRelationshipsMixin

from pypnusershub.env import ma

from apptax.taxonomie.models import (
    BibListes,
    TMedias,
    BibTypesMedia,
    Taxref,
    CorTaxonAttribut,
    BibTaxrefRangs,
    VBdcStatus,
)


class BibTypesMediaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BibTypesMedia
        include_fk = True


class TMediasSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TMedias
        include_fk = True

    media_url = fields.String()
    types = fields.Nested(BibTypesMediaSchema())


class BibListesSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BibListes
        include_fk = True

    nb_taxons = fields.Integer()


class CorTaxonAttributSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CorTaxonAttribut
        include_fk = True


class BibTaxrefRangsSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BibTaxrefRangs
        include_fk = True


class VBdcStatusSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VBdcStatus
        include_fk = True


class TaxrefSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Taxref
        include_fk = True

    medias = fields.Nested(TMediasSchema, many=True)
    attributs = fields.Nested(CorTaxonAttributSchema, many=True)
    rang = fields.Nested(BibTaxrefRangsSchema, many=False)
    status = fields.Nested(VBdcStatusSchema, many=True)
    synonymes = fields.Nested("self", many=True)
    listes = auto_field()