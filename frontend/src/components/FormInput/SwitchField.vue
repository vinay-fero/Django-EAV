<template>
  <v-switch
    v-on="$listeners"
    v-bind="$attrs"
    outlined
    class="pa-0 ma-0"
    color="accent"
    dense
    inset
    v-model="switchValue"
    hide-details="auto"
    @change="$emit('input', $event)"
  ></v-switch>
</template>

<script>
export default {
  name: "FileTag",
  value: Boolean,
  props: {
    value: {
      required: true,
    },
  },
  computed: {
    switchValue: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      },
    },
  },
};
</script>
