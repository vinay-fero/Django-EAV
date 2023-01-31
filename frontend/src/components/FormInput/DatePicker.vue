<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    transition="scale-transition"
    offset-y
    @click="menu != menu"
    @change="$emit('change')"
    min-width="auto"
    bottom
    left
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="date"
        hide-details="auto"
        append-icon="mdi-calendar"
        readonly
        dense
        outlined
        background-color="background_color"
        v-bind="{ ...attrs, ...$attrs }"
        v-on="{ ...on, $listeners }"
        :label="`${label} ${required ? ' *' : ''}`"
        :rules="[
          ...(required ? [(val) => !!val || `${label} is required`] : []),
          ...rules,
        ]"
        @click:append="menu = true"
        @click:clear="$emit('change', null)"
      ></v-text-field>
    </template>
    <v-date-picker
      v-model="date"
      :type="type"
      v-bind="$attrs"
      v-on="$listeners"
      @input="menu = false"
    ></v-date-picker>
  </v-menu>
</template>

<script>
export default {
  data() {
    return {
      menu: false,
    };
  },
  props: {
    label: {
      type: String,
    },
    value: {
      required: true,
    },
    type: {
      type: String,
    },
    required: {
      type: Boolean,
      default: false,
    },
    rules: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    date: {
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

<style></style>
