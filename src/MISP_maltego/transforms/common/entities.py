from canari.maltego.message import Entity, IntegerEntityField, StringEntityField, MatchingRule

__author__ = 'Christophe Vandeplas'
__copyright__ = 'Copyright 2018, MISP_maltego Project'
__credits__ = []

__license__ = 'AGPLv3'
__version__ = '0.1'
__maintainer__ = 'Christophe Vandeplas'
__email__ = 'christophe@vandeplas.com'
__status__ = 'Development'

__all__ = [
    'MISPEvent',
    'MISPObject',
    'MISPGalaxy'
]


class MISPEvent(Entity):
    _category_ = 'MISP'
    _namespace_ = 'misp'

    icon_url = 'file://MISP_maltego/resources/images/MISPEvent.png'
    uuid = StringEntityField('uuid', display_name='UUID', matching_rule=MatchingRule.Loose)
    id = IntegerEntityField('id', display_name='id', is_value=True)
    # date = DateEntityField('type.date', display_name='Event date')
    info = StringEntityField('info', display_name='Event info', matching_rule=MatchingRule.Loose)
    # threat_level = EnumEntityField('type.enum', choices=['Undefined', 'Low', 'Medium', 'High'], display_name='Threat Level')
    # analysis = EnumEntityField('type.enum', choices=['Initial', 'Ongoing', 'Completed'])
    # org = StringEntityField('type.str', display_name='Organisation')


class MISPObject(Entity):
    _category_ = 'MISP'
    _namespace_ = 'misp'

    icon_url = 'file://MISP_maltego/resources/images/MISPObject.png'
    uuid = StringEntityField('uuid', display_name='UUID')
    event_id = IntegerEntityField('event_id', display_name='Event ID')
    name = StringEntityField('name', display_name='Name', is_value=True)
    meta_category = StringEntityField('meta_category', display_name='Meta Category')
    description = StringEntityField('description', display_name='Description')
    comment = StringEntityField('comment', display_name='Comment')


class MISPGalaxy(Entity):
    _category_ = 'MISP'
    _namespace_ = 'misp'

    uuid = StringEntityField('uuid', display_name='UUID')
    name = StringEntityField('name', display_name='Name', is_value=True)
    description = StringEntityField('description', display_name='Description')
    cluster_type = StringEntityField('galaxy_type', display_name='Type')
    cluster_value = StringEntityField('value', display_name='Value')
    synonyms = StringEntityField('synonyms', display_name='Synonyms')
    tag_name = StringEntityField('tag_name', display_name='Tag')
