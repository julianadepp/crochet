from rest_framework import serializers
from .models import Hook, Yarn, Stitch, Gauge, Pattern

class HookSerializer(serializers.HyperlinkedModelSerializer):
    yarns = serializers.HyperlinkedRelatedField(
        view_name='yarn_info',
        many=True,
        queryset=Hook.objects.all()
    )
    size_name = serializers.CharField(source='get_size_display', read_only=True)
    yarn_ids = serializers.PrimaryKeyRelatedField(source='yarns', many=True, queryset=Yarn.objects.all())
    class Meta:
        model = Hook
        fields = ('id', 'size', 'hook_image', 'yarns', 'yarn_ids', 'size_name')


class YarnSerializer(serializers.HyperlinkedModelSerializer):
    suggested_hooks = HookSerializer(
        many=True,
        read_only=True
    )
    hooks = serializers.PrimaryKeyRelatedField(source='suggested_hooks', many=True, queryset=Hook.objects.all())
    class Meta:
        model = Yarn
        fields = ('id', 'suggested_hooks', 'hooks', 'nickname', 'weight_description', 'brand', 'material', 'weight', 'notes', 'yarn_image', )


class StitchSerializer(serializers.HyperlinkedModelSerializer):
    related_stitches = serializers.PrimaryKeyRelatedField( many=True, queryset=Stitch.objects.all())
    class Meta:
        model = Stitch
        fields = ('id', 'name', 'description', 'pattern_code', 'instructions', 'notes', 'related_stitches', 'stitch_image')

class GaugeSerializer(serializers.HyperlinkedModelSerializer):
    stitch_id = serializers.PrimaryKeyRelatedField(source='stitch', queryset=Stitch.objects.all())
    stitch = StitchSerializer(
        read_only=True
    )
    hook_id = serializers.PrimaryKeyRelatedField(source='hook', queryset=Hook.objects.all())
    hook = HookSerializer(
        read_only=True
    )
    yarn_id = serializers.PrimaryKeyRelatedField(source='yarn', queryset=Yarn.objects.all())
    yarn = YarnSerializer(
        read_only=True
    )
    
    class Meta:
        model = Gauge
        fields = ('id', 'title', 'hook', 'stitch', 'yarn', 'yarn_id', 'hook_id', 'stitch_id', 'number_of_stitches', 'notes', 'gauge_image')

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
        fields = ('id', 'name', 'hook', 'stitches', 'yarn', 'yarn_id', 'hook_id', 'stitch_id', 'gauge', 'description', 'instructions', 'notes', 'pattern_image')