import os
from pathlib import Path
import argparse
import yaml
import re

def apply_templates(template_dir, repo_name, output_dir):
    # Load yaml files from the template directory
    template_files = {str(name.name): name.read_text() for name in Path(template_dir).glob("*.yml")}

    changes_made = False

    for name, content in template_files.items():
        # Replace {{repo_name}} with the actual repo name
        rendered_workflow = re.sub(r"{{\s*repo_name\s*}}", repo_name, content)

        # Parse the rendered YAML to ensure it's valid
        parsed_yaml = yaml.safe_load(rendered_workflow)

        # Write the rendered workflow to the output directory
        output_file = Path(output_dir) / name
        output_file.parent.mkdir(parents=True, exist_ok=True)

        if not output_file.exists() or output_file.read_text() != rendered_workflow:
            output_file.write_text(rendered_workflow)
            changes_made = True
            print(f"Updated {output_file}")
        else:
            print(f"No changes needed for {output_file}")

    return changes_made

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--template_dir", type=str, default=".templates")
    parser.add_argument("--repo_name", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default=".github/workflows")
    args = parser.parse_args()

    changes_made = apply_templates(args.template_dir, args.repo_name, args.output_dir)

    # Set an output variable for use in GitHub Actions
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            print(f"changes_made={str(changes_made).lower()}", file=f)
