<template>
  <v-select
    v-model="selectedItems"
    :items="items"
    outlined
    :item-text="itemText"
    :item-value="itemValue"
    background-color="background_color"
    :dense="dense"
    ref="list"
    hide-details="auto"
    :label="label"
    :error-messages="errorMessages"
    @blur.prevent="$emit('blur')"
    v-on="$listeners"
    :clearable="isClearable"
    v-bind="$attrs"
    :menu-props="{ offsetY: true }"
  >
    <template
      v-slot:selection="{ item, index }"
      v-if="$attrs && 'multiple' in $attrs && $attrs['multiple']"
    >
      <div>
        <span class="d-none">{{ item }}</span>
        <span v-if="index === 0" class="text-caption pl-2 text-capitalize">
          {{ selectedItems.length }} Selected
        </span>
      </div>
    </template>
    <template v-slot:prepend-item>
      <v-list-item v-if="isSearchRequired">
        <InputField
          class="mb-2 pt-1"
          v-model="searchInput"
          label="Search here..."
          clearable
          hide-details
          prepend-inner-icon="mdi-magnify"
        />
      </v-list-item>
      <v-list-item
        ripple
        @click="
          toggleSelectAll();
          onChanges();
        "
        v-if="$attrs && $attrs['multiple']"
      >
        <v-list-item-action>
          <v-icon
            :color="
              selectedItems && selectedItems.length > 0 ? 'indigo darken-4' : ''
            "
          >
            {{ isAllSelected ? "mdi-checkbox-marked" : "mdi-minus-box" }}
          </v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="text-capitalize text-left">
            select all
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider class="mt-2"></v-divider>
    </template>
    <template #prepend-inner>
      <slot name="prepend-inner" />
    </template>
  </v-select>
</template>

<script>
export default {
  props: {
    isSearchRequired: {
      type: Boolean,
      default: true,
    },
    itemsList: {
      type: Array,
      required: true,
    },
    itemText: {
      type: String,
      default: "text",
    },
    itemValue: {
      type: String,
      default: "value",
    },
    label: {
      type: String,
      default: "Select Items",
    },
    dense: {
      type: Boolean,
      default: true,
    },
    value: {
      required: true,
    },
    errorMessages: {
      type: [Array, Object, String, Number],
    },
    isClearable: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      searchInput: null,
      isAllSelected: false,
    };
  },
  computed: {
    selectedItems: {
      get() {
        return this.value;
      },
      set(val) {
        if (this.itemsList && val && this.itemsList.length == val.length) {
          this.isAllSelected = true;
        } else {
          this.isAllSelected = false;
        }
        this.$emit("input", val);
      },
    },
    items() {
      if (this.searchInput) {
        let search = this.searchInput.toLowerCase();
        return this.itemsList.filter((item) => {
          if (typeof item == typeof {}) {
            return item[this.itemText].toLowerCase().indexOf(search) > -1;
          } else {
            return item.toLowerCase().indexOf(search) > -1;
          }
        });
      } else {
        return this.itemsList;
      }
    },
  },
  methods: {
    onChanges() {
      setTimeout(() => {
        this.$emit("change", this.selectedItems);
      }, 50);
    },
    toggleSelectAll() {
      this.isAllSelected = !this.isAllSelected;
      if (this.isAllSelected) {
        if (
          this.$attrs &&
          "return-object" in this.$attrs &&
          this.$attrs["return-object"]
        ) {
          this.selectedItems = this.itemsList;
        } else {
          this.selectedItems = this.itemsList.map((item) => {
            if (typeof item == typeof {}) {
              return item[this.itemValue];
            } else {
              return item;
            }
          });
        }
      } else {
        this.selectedItems = [];
      }
    },
  },
};
</script>

<style></style>
