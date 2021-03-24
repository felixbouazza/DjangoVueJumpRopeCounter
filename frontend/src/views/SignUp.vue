<template>

    <div>
        <h1>Sign Up</h1>
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

            <button>Sign Up</button>
        </form>
    </div>


</template>

<script>
import axios from "axios"

export default {
    name: 'SignUp',
    data () {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                password: this.password
            }
            axios
                .post("/api/v1/users/", formData)
                .then(response => {
                    console.log(response)
                    this.$router.push('/log-in')
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