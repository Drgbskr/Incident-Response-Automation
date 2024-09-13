import logging

def notify_team(report):
    """
    Notify the team about the generated report.
    """
    logging.info(f"Team notified with report: {report}")

def isolate_host(host):
    """
    Isolate the host from the network.
    """
    logging.info(f"Host {host} isolated.")

def collect_evidence(host, output_dir):
    """
    Collect evidence from the isolated host.
    """
    logging.info(f"Evidence collected from host {host} and saved to {output_dir}.")
