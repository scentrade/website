module.exports = function(grunt) {

  grunt.initConfig({

    pkg: grunt.file.readJSON('package.json'),

    less: {
      development: {
        options: {
          paths: ["scentrade/static/stylesheets"]
        },
        files: {
          "scentrade/static/stylesheets/scentrade.css": "scentrade/static/stylesheets/_scentrade.less"
        }
      }
    },

    django_compressor: {
      js: {
        options: {
          startTag: '<!--SCRIPTS-->',
          endTag: '<!--SCRIPTS END-->',
          excludedDirs: [
            'node_modules/'
          ],
          generateJsSourceMaps: true
        }
      },
      css: {
        options: {
          startTag: '<!--STYLES-->',
          endTag: '<!--STYLES END-->',
          excludedDirs: [
            'node_modules/'
          ]
        }
      }
    },

    watch: {
      files: ['scentrade/static/stylesheets/**/*.less'],
      tasks: ['less:development']
    }

  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('assemble-less');
  grunt.loadNpmTasks('grunt-django-compressor');

  grunt.registerTask('production', [
    'django_compressor'
  ]);

};