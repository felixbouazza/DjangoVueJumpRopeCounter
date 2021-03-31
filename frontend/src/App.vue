<template>
  <nav>
    <router-link to="/"><strong>JumpRopeCounter</strong></router-link>
    <div class="navbarlist">
      <template v-if="$store.state.isAuthenticated">
        <router-link to="/dashboard">Dashboard</router-link>
        <router-link to="/dashboard/sessions">Sessions</router-link>
        <div class="items">
          <router-link to="/dashboard/my-account">MyAccount</router-link>
          <button @click="logout()" id="log-out">LogOut</button>
        </div>
      </template>

      <template v-else>
        <router-link to="/">Home</router-link>
        <div class="items">
          <router-link to="/sign-up" id="sign-up"><strong>Sign up</strong></router-link>
          <router-link to="/log-in" id="log-in"><strong>Log in</strong></router-link>
        </div>
      </template>
    </div>
  </nav>
  <section class="section">
    <router-view/>
  </section>


  <footer class="footer">
    <p>Copyright (c) 2021</p>
  </footer>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'App',
    beforeCreate() {
      this.$store.commit('initializeStore')
      
      const token = this.$store.state.token
      if (token) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
      } else {
        axios.defaults.headers.common['Authorization'] = ''
      }
    },
    methods: {
      logout() {
        axios
            .post("/api/v1/token/logout")
            .then(response => {
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                this.$store.commit('removeToken')
                this.$router.push('/')
            })
            .catch(error => {
                if (error.response) {
                    console.log(JSON.stringify(error.response.data))
                } else if (error.message) {
                    console.log(JSON.stringify(error.message))
                } else {
                    console.log(JSON.stringify(error))
                }
            })
        }
    }
  }
</script>


<style lang="scss">
#sign-up {
  background-color: green;
  border-radius: 5%;
  padding: 4px 8px;
  color: white;
  text-decoration: none;
}

#log-in {
  background-color: red;
  border-radius: 5%;
  padding: 4px 8px;
  color: white;
  text-decoration: none;
}

#log-out {
  background-color: red;
  border-radius: 5%;
  padding: 4px 8px;
  color: white;
  text-decoration: none;
}
</style>
