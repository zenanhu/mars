<template>
  <div id="app">
    <v-app id="inspire">
        <v-navigation-drawer 
            v-model="drawer"
            clipped persistent enable-resize-watcher app>

            <v-list dense>
                <v-list-tile :to="{path: '/'}" :route="true">
                    <v-list-tile-action>
                        <v-icon>home</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title>Home</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-list-tile to="/dict" :route="true">
                    <v-list-tile-action>
                        <v-icon>font_download</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title>Dictionary</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-list-tile to="/bmi" :route="true">
                    <v-list-tile-action>
                        <v-icon>accessibility</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title>BMI</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-list-tile to="/about" :route="true">
                    <v-list-tile-action>
                        <v-icon>free_breakfast</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title>About</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>

        <v-toolbar color="indigo" dark clipped-left fixed app>
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title>Mars</v-toolbar-title>
        </v-toolbar>

        <main>
            <v-content>
                <v-container fluid fill-height>
                    <router-view/>
                </v-container>
            </v-content>
        </main>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'app',
  data: () => ({
    drawer: true
  })
}
</script>

<style>
#app {
}
</style>
