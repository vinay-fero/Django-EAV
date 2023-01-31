<template>
  <v-text-field
    hide-details="auto"
    autocomplete="new-password"
    v-on="$listeners"
    :background-color="backgroundColor"
    v-bind="$attrs"
    dense
    :label="`${label} ${required ? ' *' : ''}`"
    :rules="[
      ...(required ? [(val) => !!val || `${label} is required`] : []),
      ...rules,
    ]"
    outlined
  ></v-text-field>
</template>

<script>
export default {
  name: "InputTag",
  props: {
    required: {
      type: Boolean,
      default: false,
    },
    label: String,
    rules: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    backgroundColor() {
      return this.$attrs && this.$attrs["background-color"]
        ? this.$attrs["background-color"]
        : "background_color";
    },
  },
};
</script>
