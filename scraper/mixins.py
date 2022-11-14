class FlattenMixin(object):
    """Flatens the specified related objects in this representation"""
    def to_representation(self, obj):
        assert hasattr(self.Meta, 'flatten'), (
            'Class {serializer_class} missing "Meta.flatten" attribute'.format(
                serializer_class=self.__class__.__name__
            )
        )

        rep = super(FlattenMixin, self).to_representation(obj)

        for field, serializer_class in self.Meta.flatten:
            serializer = serializer_class(context = self.context)
            objrep = serializer.to_representation(getattr(obj, field))

            for key in objrep:
                rep[field + "_" + key] = objrep[key]
        return rep