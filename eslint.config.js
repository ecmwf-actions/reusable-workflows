// eslint.config.js
import yaml from 'eslint-plugin-yaml';
import yamlParser from 'yaml-eslint-parser';

export default [
  {
    files: ["**/*.yml"],
    plugins: {
      yaml
    },
    languageOptions: {
      parser: yamlParser
    },
    rules: {
      // Add any YAML-specific rules here if needed
    }
  },
];
