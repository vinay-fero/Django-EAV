<template>
  <div
    @dragover="dragover"
    @dragleave="dragleave"
    @drop="drop"
    :style="`height:${height}`"
    class="px-3 py-12 d-flex justify-center algin-center app-relative w-100"
    :class="files && files.length > 0 ? '' : 'background_color'"
  >
    <form ref="myForm">
      <input
        type="file"
        :multiple="multiple"
        name="file"
        id="fileInput"
        class="hidden-input d-none"
        @change="onChange"
        ref="fileUpload"
        :accept="accept"
      />
    </form>
    <div v-if="files && files.length > 0" class="d-flex align-center">
      <v-icon
        color="error"
        style="position: absolute; top: 6px; right: 5px"
        @click="removeFile"
        >mdi-close-box</v-icon
      >
      <v-chip
        label
        outlined
        color="primary"
        class="text-caption text-capitalize"
      >
        {{ files.length }} Selected Files
      </v-chip>
    </div>

    <div v-else class="d-flex flex-column algin-center justify-center">
      <h6 class="text-caption text-capitalize text-center">drag and Drop</h6>
      <h5 class="text-center py-2">OR</h5>
      <PrimaryButton name="File Upload" @click="$refs.fileUpload.click()" />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    height: {
      default: "200px",
    },
    accept: {
      default: ".pdf,.jpg,.jpeg,.png",
    },
    multiple: {
      required: false,
      default: false,
    },
  },
  data() {
    return {
      isDragging: false,
      files: [],
    };
  },
  methods: {
    removeFile() {
      this.files = [];
      this.$refs.myForm.reset();
      this.$emit("selectedFile", this.multiple ? [] : null);
    },
    onChange() {
      this.files = this.$refs.fileUpload.files;
      let newFile = this.multiple
        ? [...this.$refs.fileUpload.files]
        : this.$refs.fileUpload.files[0];
      this.$emit("selectedFile", newFile);
    },
    dragover(e) {
      e.preventDefault();
      this.isDragging = true;
    },
    dragleave() {
      this.isDragging = false;
    },
    drop(e) {
      e.preventDefault();
      this.$refs.fileUpload.files = e.dataTransfer.files;
      this.onChange();
      this.isDragging = false;
    },
  },
};
</script>
