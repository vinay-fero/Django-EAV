<template>
  <v-textarea
    v-on="$listeners"
    v-bind="$attrs"
    outlined
    dense
    background-color="background_color"
    hide-details="auto"
    :label="`${label} ${required ? ' *' : ''}`"
    :rules="[
      ...(required ? [(val) => !!val || `${label} is required`] : []),
      ...rules,
    ]"
  ></v-textarea>
</template>

<script>
export default {
  name: "FileTag",
  props: {
    required: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
    },
    rules: {
      type: Array,
      default: () => [],
    },
  },
};
</script>
