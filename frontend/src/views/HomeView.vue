<template>
  <div v-if="organizationList && organizationList.length > 0">
    <div
      v-for="(value, key, index) in organizationList[1].order_fields"
      :key="index"
    >
      <v-col class="6">
        <FormComponentWrapper
          :inputType="value"
          v-model="organizationForm[key]"
        />
      </v-col>
    </div>
    <div>
      <pre>{{ organizationForm }}</pre>
    </div>
    <div>
      <v-btn @click="checkTheData">Submit</v-btn>
    </div>
  </div>
</template>

<script>
import { getData } from "@/utils/fetchWrapper";
import FormComponentWrapper from "@/components/FormInput/FormComponentWrapper.vue";

export default {
  components: { FormComponentWrapper },
  name: "HomeView",
  data() {
    return {
      organizationList: [],
      organizationForm: {},
    };
  },
  methods: {
    checkTheData() {
      console.log(this.organizationForm);
    },
    getOrganizationList() {
      getData("http://127.0.0.1:8000/api/v1/organization/")
        .then((res) => {
          let organizationList = res.map((obj) => {
            console.log(obj);
            for (let key in obj.order_fields) {
              obj.order_fields[key]["label"] = key.replace(/_/g, " ");
            }
            return obj;
          });
          this.organizationList = organizationList;
          console.log(this.organizationList);
        })
        .catch((err) => console.error(err));
    },
    getCustomComponent(obj) {
      let componentIs = "InputField";
      if (obj.type == "date") {
        componentIs = "DatePicker";
      }
      return componentIs;
    },
  },
  mounted() {
    this.getOrganizationList();
  },
};
</script>
