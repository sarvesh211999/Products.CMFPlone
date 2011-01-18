from setuptools import setup, find_packages
import os.path

version = '4.1a2'

setup(name='Products.CMFPlone',
      version=version,
      description="The Plone Content Management System (core)",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "CHANGES.txt")).read(),
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        ],
      keywords='Plone CMF python Zope',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://plone.org/',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
          'Products.PloneTestCase',
          'zope.testing',
        ]),
      install_requires=[
          'setuptools',
          'Acquisition',
          'DateTime',
          'ExtensionClass',
          'Products.Archetypes',
          'Products.ATContentTypes',
          'Products.CMFActionIcons',
          'Products.CMFCalendar',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.CMFDiffTool',
          'Products.CMFDynamicViewFTI',
          'Products.CMFEditions',
          'Products.CMFFormController',
          'Products.CMFQuickInstallerTool',
          'Products.CMFUid',
          'Products.DCWorkflow',
          'Products.ExtendedPathIndex',
          'Products.ExternalEditor',
          'Products.GenericSetup >=1.4',
          'Products.MimetypesRegistry',
          'Products.PasswordResetTool',
          'Products.PlacelessTranslationService',
          'Products.PloneLanguageTool',
          'Products.PlonePAS',
          'Products.PluggableAuthService',
          'Products.PluginRegistry',
          'Products.PortalTransforms',
          'Products.ResourceRegistries',
          'Products.statusmessages',
          'Products.TinyMCE',
          'Zope2 > 2.13.0',
          'ZODB3',
          'archetypes.kss',
          'archetypes.referencebrowserwidget',
          'borg.localrole',
          'five.localsitemanager',
          'five.customerize',
          'kss.core',
          'plone.app.blob',
          'plone.app.contentmenu >= 1.1.6dev-r22380',
          'plone.app.content',
          'plone.app.contentrules',
          'plone.app.controlpanel',
          'plone.app.customerize',
          'plone.app.folder',
          'plone.app.form',
          'plone.app.i18n',
          'plone.app.jquerytools',
          'plone.app.kss',
          'plone.app.layout >=1.1.7dev-r23744',
          'plone.app.linkintegrity >=1.0.3',
          'plone.app.locales',
          'plone.app.portlets',
          'plone.app.redirector',
          'plone.app.registry',
          'plone.app.users',
          'plone.app.upgrade',
          'plone.app.uuid',
          'plone.app.viewletmanager',
          'plone.app.vocabularies',
          'plone.app.workflow',
          'plone.browserlayer >= 1.0rc4',
          'plone.contentrules',
          'plone.fieldsets',
          'plone.i18n',
          'plone.indexer',
          'plone.intelligenttext',
          'plone.locking',
          'plone.memoize',
          'plone.portlets',
          'plone.protect > 1.0',
          'plone.registry',
          'plone.session',
          'plone.theme',
          'plone.portlet.collection',
          'plone.portlet.static',
          'plonetheme.classic',
          'plonetheme.sunburst',
          'transaction',
          'wicked',
          'z3c.autoinclude',
          'zope.app.container',
          'zope.app.locales >= 3.6.0',
          'zope.app.publication',
          'zope.component',
          'zope.deferredimport',
          'zope.deprecation',
          'zope.dottedname',
          'zope.event',
          'zope.i18n',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.location',
          'zope.pagetemplate',
          'zope.publisher',
          'zope.site',
          'zope.structuredtext',
          'zope.tal',
          'zope.tales',
      ],
      )
