<template>
  <div>
    {{ $attrs }}
    <InputField
      v-if="inputType.type == 'text'"
      :label="inputType.label"
      :required="inputType.is_required"
      v-bind="$attrs"
    />
    <InputField
      v-else-if="inputType.type == 'integer'"
      type="number"
      :label="inputType.label"
      :required="inputType.is_required"
      v-bind="$attrs"
    />
    <InputField
      v-else-if="inputType.type == 'float'"
      :label="inputType.label"
      :required="inputType.is_required"
      type="number"
      step="0.01"
      v-bind="$attrs"
    />
    <InputField
      v-else-if="inputType.type == 'date'"
      :label="inputType.label"
      v-bind="$attrs"
      type="date"
    />
  </div>
</template>

<script>
export default {
  props: {
    inputType: {
      required: true,
    },
  },
};
</script>

<style></style>
