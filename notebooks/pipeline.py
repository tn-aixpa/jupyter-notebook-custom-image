from digitalhub_runtime_kfp.dsl import pipeline_context


def my_pipeline(di_key):
    with pipeline_context() as pc:
        s1 = pc.step(
            name="step1",
            function="downloader",
            action="job",
            inputs={"url": di_key},
            outputs={"dataset": "dataset"},
        )

        s2_1 = pc.step(
            name="step2.1",
            function="process-spire",
            action="job",
            inputs={"di": s1.outputs["dataset"]},
            outputs={"dataset-spire": "dataset-spire"},
        )

        s2_2 = pc.step(
            name="step2.2",
            function="process-measure",
            action="job",
            inputs={"di": s1.outputs["dataset"]},
            outputs={"dataset-measures": "dataset-measures"},
        )

        return s2_1.outputs["dataset-spire"], s2_2.outputs["dataset-measures"]
