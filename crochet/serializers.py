from rest_framework import serializers
from .models import Hook, Yarn, Stitch, Gauge, Pattern

class HookSerializer(serializers.HyperlinkedModelSerializer):
    yarns = serializers.HyperlinkedRelatedField(
        view_name='yarn_info',
        many=True,
        read_only=True
    )
    size_name = serializers.CharField(source='get_size_display', read_only=True)
    class Meta:
        model = Hook
        fields = ('id', 'size', 'hook_image', 'yarns', 'size_name')


class YarnSerializer(serializers.HyperlinkedModelSerializer):
    suggested_hooks = HookSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Yarn
        fields = ('id', 'suggested_hooks', 'nickname', 'weight_description', 'brand', 'material', 'weight', 'notes', 'yarn_image', )


class StitchSerializer(serializers.HyperlinkedModelSerializer):
    related_stitches = serializers.HyperlinkedRelatedField(
        view_name='stitch_info',
        many=True,
        read_only=True
    )
    class Meta:
        model = Stitch
        fields = ('id', 'name', 'description', 'pattern_code', 'instructions', 'notes', 'related_stitches', 'stitch_image')

class GaugeSerializer(serializers.HyperlinkedModelSerializer):
    stitch = StitchSerializer(
        read_only=True
    )
    hook = HookSerializer(
        read_only=True
    )
    yarn = YarnSerializer(
        read_only=True
    )
    
    class Meta:
        model = Gauge
        fields = ('id', 'title', 'hook', 'stitch', 'yarn', 'number_of_stitches', 'notes', 'gauge_image')

class PatternSerializer(serializers.HyperlinkedModelSerializer):
    stitches = StitchSerializer(
        read_only=True,
        many=True
    )
    hook = HookSerializer(
        read_only=True
    )
    yarn = YarnSerializer(
        many=True,
        read_only=True
    )
    gauge = GaugeSerializer(
        read_only=True
    )
    
    class Meta:
        model = Pattern
        fields = ('id', 'name', 'hook', 'stitches', 'yarn', 'gauge', 'description', 'instructions', 'notes', 'pattern_image')