import auto_configs as conf
import generate_fonts as gen
import generate_simsun as simsun
import copy_result as copy

if __name__ == '__main__':

    gen.gen_regular()
    print('========> Regular generated')
    gen.gen_bold()
    print('========> Bold generated')
    gen.gen_light()
    print('========> Light generated')
    simsun.gen_simsun_ttc()
    print('========> Simsun ttc generated')
    simsun.gen_simsun_ext()
    print('========> Simsun ext generated')
    copy.copy_result()
    print('========> Copy Finished')
