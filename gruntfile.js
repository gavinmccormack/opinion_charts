module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration goes here.

    concat: {
      app: {
        src: ['myproject/static/js/app/**/*.js'],
        dest: 'build/static/js/app.js'
      },
      vendor: {
        src: ['myproject/static/js/vendor/**/*.js'],
        dest: 'build/static/js/lib.js'
      }
    },

    sass: {
      dev: {
        options: {
          includePaths: ['bower_components/foundation/scss']
        },
        files: {
          'build/static/css/screen.css': 'myproject/static/scss/screen.scss'
        }
      },
      deploy: {
        options: {
          includePaths: ['bower_components/foundation/scss'],
          outputStyle: 'compressed'
        },
        files: {
          'build/static/css/screen.min.css': 'myproject/static/scss/screen.scss'
        }
      }
    },

    watch: {
            options: {livereload: true}
            javascript: {
                files: ['myproject/static/js/app/**/*.js'],
                tasks: ['concat']
            },
            sass: {
                files: 'myproject/static/scss/**/*.scss',
                tasks: ['sass:dev']
            }
        }
  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', []);

};