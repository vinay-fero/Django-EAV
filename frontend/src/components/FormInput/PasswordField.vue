<template>
  <v-text-field
    outlined
    hide-details="auto"
    dense
    v-bind="$attrs"
    v-on="$listeners"
    background-color="background_color"
    prepend-inner-icon="mdi-lock-outline"
    :append-icon="oldPassword ? 'mdi-eye' : 'mdi-eye-off'"
    :type="oldPassword ? 'text' : 'password'"
    :label="`${label} ${required ? ' *' : ''}`"
    :rules="[
      ...(required ? [(val) => !!val || `${label} is required`] : []),
      ...rules,
    ]"
    autocomplete="new-password"
    @click:append="oldPassword = !oldPassword"
  />
</template>

<script>
export default {
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
  data() {
    return {
      oldPassword: false,
    };
  },
};
</script>

<style></style>
