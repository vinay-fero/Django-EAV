<template>
  <v-file-input
    outlined
    prepend-icon=""
    append-icon="mdi-paperclip"
    :truncate-length="truncateLength"
    background-color="background_color"
    hide-details="auto"
    show-size
    v-bind="$attrs"
    v-on="$listeners"
    @change="$emit('input', $event)"
  ></v-file-input>
</template>

<script>
export default {
  name: "FileTag",
  props: {
    truncateLength: {
      default: 50,
    },
  },
};
</script>
