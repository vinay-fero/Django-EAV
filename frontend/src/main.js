import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import InputField from "@/components/FormInput/InputField.vue";
import SelectField from "@/components/FormInput/SelectField.vue";
import FileField from "@/components/FormInput/FileField.vue";
import SwitchField from "@/components/FormInput/SwitchField.vue";
import TextAreaField from "@/components/FormInput/TextAreaField.vue";
import DatePicker from "@/components/FormInput/DatePicker.vue";
import PasswordField from "@/components/FormInput/PasswordField.vue";
import FileUpload from "@/components/FormInput/FileUpload.vue";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

Vue.component("FileUpload", FileUpload);
Vue.component("InputField", InputField);
Vue.component("SelectField", SelectField);
Vue.component("FileField", FileField);
Vue.component("SwitchField", SwitchField);
Vue.component("TextAreaField", TextAreaField);
Vue.component("DatePicker", DatePicker);
Vue.component("PasswordField", PasswordField);

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
