<template>

    <h1>Log In</h1>

    <form @submit.prevent="submitForm">

        <label>Email</label>
        <div>
            <input type="email" name="username" v-model="username">
        </div>

        <label>Password</label>
        <div>
            <input type="password" name="password" v-model="password">
        </div>

        <div v-if="errors.length">
            <p 
                v-for="error in errors"
                v-bind:key="error"
            >
            {{ error }}
            </p>
        </div>
        <button>Log In</button>
    </form>

</template>

<script>
import axios from "axios"

export default {
    name: "LogIn",
    data () {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        submitForm(e) {

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token
                    localStorage.setItem('token', token)
                    this.$router.push('/dashboard')
                })
                .catch(error => {
                    if(error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property} : ${error.response.data[property]}`)
                        }
                    }
                })
        }
    }
}
</script>