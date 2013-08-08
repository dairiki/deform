from zope.deprecation import __show__, deprecated

from .field import Field # API

from .form import Form # API
from .form import Button # API

from .exception import ValidationFailure # API
from .exception import TemplateError # API

__show__.off()
from .schema import Set # API
__show__.on()
from .schema import FileData # API

from .template import ZPTRendererFactory # API
from .template import default_renderer # API

deprecated(
    'Set',
    'deform.Set is deprecated as of the release of Colander > 1.0a1, which '
    'includes its own Set class.  colander.Set is not exactly a drop-in '
    'replacement (it has no allow_empty constructor argument), but you should '
    'switch to it as soon as possible.  The deform.Set class will be removed '
    'in Deform 1.1+'
    )
