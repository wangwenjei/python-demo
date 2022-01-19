from rest_framework.renderers import CoreJSONRenderer, coreapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.generators import LinkNode, insert_into
from rest_framework_swagger import renderers


class MySchemaGenerator(SchemaGenerator):

    def get_links(self, request=None):
        # from rest_framework.schemas.generators import LinkNode,
        links = LinkNode()

        paths = []
        view_endpoints = []
        for path, method, callback in self.endpoints:
            view = self.create_view(callback, method, request)
            path = self.coerce_path(path, method, view)
            paths.append(path)
            view_endpoints.append((path, method, view))

        # Only generate the path prefix for paths that will be included
        if not paths:
            return None
        prefix = self.determine_path_prefix(paths)

        for path, method, view in view_endpoints:
            if not self.has_view_permissions(path, method, view):
                continue
            link = view.schema.get_link(path, method, base_url=self.url)
            link._fields += self.get_core_fields(view)

            subpath = path[len(prefix):]
            keys = self.get_keys(subpath, method, view)

            insert_into(links, keys, link)

        return links

    # Take our custom parameters from the class and pass them to swagger to generate the interface documentation.
    @staticmethod
    def get_core_fields(view):
        return getattr(view, 'core_api_fields', ())


class SwaggerSchemaView(APIView):
    _ignore_model_permissions = True
    exclude_from_schema = True

    permission_classes = [AllowAny]
    renderer_classes = [
        CoreJSONRenderer,
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = MySchemaGenerator(title='API',
                                      description='''api文档''')

        schema = generator.get_schema(request=request)

        return Response(schema)


def DocParam(name="default", location="query",
             required=True, description=None, type="string",
             schema=None, example=None,
             *args, **kwargs):
    """
    构造参数
    :param name: Field name
    :param location: Parameter input method E.g: query, header, from, fromData...
    :param required: Enter Field True or False
    :param description: Parameter Description
    :param type: Parameter format E.g: string, file...
    :param args:
    :param kwargs:
    :return:
    """
    return coreapi.Field(name=name, location=location,
                         required=required, description=description,
                         type=type)
