<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-email-group"
                  label="Login:"
                  label-for="form-email-input">
        <b-form-input id="form-email-input"
                      type="email"
                      v-model="loginForm.email"
                      required
                      placeholder="Enter email">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-password-group"
                    label="Password:"
                    label-for="form-password-input">
        <b-form-input id="form-password-input"
                      type="text"
                      v-model="loginForm.password"
                      required
                      placeholder="Enter password">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      info: null,
      loginForm: {
        email: '',
        password: '',
      },
    };
  },
  methods: {
    login(payload) {
      const path = 'http://127.0.0.1:5000/login';
      axios.post(path, payload)
        .then((response) => {
          this.info = response.data;
          this.$router.push('/');
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error);
          this.$router.push('/error');
        });
    },
    initForm() {
      this.loginForm.email = '';
      this.loginForm.password = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        email: this.loginForm.email,
        password: this.loginForm.password,
      };
      this.login(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
};
</script>
